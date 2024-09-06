import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input, Embedding, LSTM, Dropout, Dense, add
import matplotlib.pyplot as plt
from PIL import Image


def load_coco_data(annotations_file, image_folder):
    with open(annotations_file, 'r') as f:
        annotations = json.load(f)
    
    image_paths = {}
    captions = {}
    for annot in annotations['annotations']:
        img_id = annot['image_id']
        caption = 'startseq ' + annot['caption'] + ' endseq'
        if img_id not in captions:
            captions[img_id] = []
        captions[img_id].append(caption)
    
    for img in annotations['images']:
        image_paths[img['id']] = os.path.join(image_folder, img['file_name'])
    
    return image_paths, captions


image_paths, captions = load_coco_data('path_to_annotations/captions_train2014.json', 'path_to_images/train2014')


def extract_features(model, image_paths):
    features = {}
    for img_id, img_path in image_paths.items():
        img = Image.open(img_path).resize((299, 299))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = tf.keras.applications.inception_v3.preprocess_input(img)
        feature = model.predict(img, verbose=0)
        features[img_id] = feature
    return features


base_model = InceptionV3(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)


features = extract_features(model, image_paths)

all_captions = []
for key, val in captions.items():
    for caption in val:
        all_captions.append(caption)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = max(len(caption.split()) for caption in all_captions)


def create_sequences(tokenizer, max_length, desc_list, photo):
    X1, X2, y = [], [], []
    for desc in desc_list:
        seq = tokenizer.texts_to_sequences([desc])[0]
        for i in range(1, len(seq)):
            in_seq, out_seq = seq[:i], seq[i]
            in_seq = pad_sequences([in_seq], maxlen=max_length)[0]
            out_seq = to_categorical([out_seq], num_classes=vocab_size)[0]
            X1.append(photo)
            X2.append(in_seq)
            y.append(out_seq)
    return np.array(X1), np.array(X2), np.array(y)


def data_generator(captions, features, tokenizer, max_length, batch_size):
    while True:
        X1, X2, y = [], [], []
        for key, desc_list in captions.items():
            photo = features[key][0]
            in_img, in_seq, out_word = create_sequences(tokenizer, max_length, desc_list, photo)
            for i in range(len(in_img)):
                X1.append(in_img[i])
                X2.append(in_seq[i])
                y.append(out_word[i])
            if len(X1) >= batch_size:
                yield [[np.array(X1), np.array(X2)], np.array(y)]
                X1, X2, y = [], [], []


def define_model(vocab_size, max_length):
    inputs1 = Input(shape=(2048,))
    fe1 = Dropout(0.5)(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)

    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
    se2 = Dropout(0.5)(se1)
    se3 = LSTM(256)(se2)

    decoder1 = add([fe2, se3])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model



def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'startseq'
    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = tokenizer.index_word[yhat]
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    return in_text


model = define_model(vocab_size, max_length)


batch_size = 64
steps = len(captions) // batch_size
generator = data_generator(captions, features, tokenizer, max_length, batch_size)

model.fit(generator, epochs=20, steps_per_epoch=steps, verbose=2)

model.save('image_captioning_model.h5')


photo = extract_features(model, {'new_image.jpg': 'path_to_new_image.jpg'})['new_image.jpg']
description = generate_desc(model, tokenizer, photo, max_length)
print(description)
