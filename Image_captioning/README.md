# Image Captioning Model

This project implements an image captioning model that generates captions for images using a combination of CNNs (InceptionV3) and RNNs (LSTM). The model is trained on the COCO dataset and aims to predict captions based on input images.

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Caption Generation](#caption-generation)
- [Usage](#usage)
- [Results](#results)
- [Future Improvements](#future-improvements)

## Installation

To run this project, you need to have Python 3.x installed along with the following dependencies:

### Required Libraries
Install the required libraries using `pip`:

```bash
pip install tensorflow numpy matplotlib pillow
```

### Additional Setup
- Download the COCO 2014 image dataset from the [official website](https://cocodataset.org/#download).
- Download the annotations file `captions_train2014.json` from the COCO dataset page.

## Dataset

The model uses the COCO 2014 dataset for image captioning, which contains images along with human-annotated captions. Each image has 5 associated captions.

Place the dataset in appropriate folders:

```
|-- path_to_images
    |-- train2014
|-- path_to_annotations
    |-- captions_train2014.json
```

## Model Architecture

The model consists of two parts:
1. **CNN (InceptionV3)**: Pre-trained InceptionV3 is used to extract features from the images.
2. **RNN (LSTM)**: The LSTM network is used to generate captions based on the features extracted by the CNN.

### CNN (InceptionV3)
The pre-trained InceptionV3 model is used to extract features from images. The last fully connected layer is removed, and the extracted 2048-dimensional feature vector is passed into the LSTM.

### LSTM
The LSTM is used to process the image features and the tokenized captions. The caption is broken down into sequences, and the model is trained to predict the next word based on the previous sequence of words.

## Training

The model is trained by generating sequences from the captions, tokenizing the words, and using them to train the LSTM network to predict the next word in the caption. The captions are tokenized using `keras.preprocessing.text.Tokenizer`.

### Training Steps

1. **Load and preprocess the dataset**: 
   The `load_coco_data` function loads image paths and associated captions from the COCO annotations.
   
2. **Extract features**: 
   The `extract_features` function extracts image features using the InceptionV3 model.

3. **Create sequences**: 
   The `create_sequences` function tokenizes and pads the captions, and pairs them with the image features.

4. **Train the model**:
   The model is trained using the `fit` function with a generator created by `data_generator`.

## Caption Generation

To generate a caption for a new image, the following steps are followed:

1. Extract features from the image using the pre-trained InceptionV3 model.
2. Use the trained LSTM model to generate the next word in the caption sequence until the model predicts the 'endseq' token.

### Example Usage:

```python
photo = extract_features(model, {'new_image.jpg': 'path_to_new_image.jpg'})['new_image.jpg']
description = generate_desc(model, tokenizer, photo, max_length)
print(description)
```

This will generate a caption for the given image.

## Results

The model generates captions that describe the contents of the image. Here are some example outputs:

- Image: `dog.jpg`
  - Generated Caption: *"startseq a dog is running in the grass endseq"*

- Image: `cat.jpg`
  - Generated Caption: *"startseq a cat is sitting on the chair endseq"*

## Future Improvements

- **Attention Mechanism**: Implement an attention mechanism to improve caption generation by focusing on different parts of the image while generating captions.
- **Beam Search**: Use beam search to improve the quality of generated captions by considering multiple caption hypotheses.
- **Better Tokenization**: Improve tokenizer efficiency by handling out-of-vocabulary words and special characters better.
- **Transfer Learning**: Experiment with other pre-trained models (ResNet, EfficientNet) for feature extraction.

