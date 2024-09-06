import pandas as pd
from surprise import Dataset
from surprise import KNNBasic
from surprise import accuracy
from surprise.model_selection import train_test_split

def get_recommendations(user_id, num_recommendations=10):
    all_movie_ids = trainset.all_items()
    watched_movie_ids = [j for (j, _) in trainset.ur[trainset.to_inner_uid(user_id)]]
    unseen_movie_ids = [movie_id for movie_id in all_movie_ids if movie_id not in watched_movie_ids]
    predictions = [algo.predict(user_id, trainset.to_raw_iid(movie_id)) for movie_id in unseen_movie_ids]
    predictions.sort(key=lambda x: x.est, reverse=True)
    top_recommendations = predictions[:num_recommendations]
    recommended_movie_ids = [int(pred.iid) for pred in top_recommendations]
    recommended_ratings = [pred.est for pred in top_recommendations]
    recommended_movies = movies_df[movies_df['movie_id'].isin(recommended_movie_ids)]
    return recommended_movies['title'].tolist(), recommended_ratings


data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=0.25)
algo = KNNBasic(sim_options={'user_based': True})
algo.fit(trainset)
predictions = algo.test(testset)
rmse = accuracy.rmse(predictions)
movies_df = pd.read_csv('http://files.grouplens.org/datasets/movielens/ml-100k/u.item',sep='|', encoding='latin-1', header=None, usecols=[0, 1], names=['movie_id', 'title'])

userinputid=int(input("Enter your User ID: "))
user_id = str(userinputid)
recommended_movies, recommended_ratings = get_recommendations(user_id)

print("Recommended movies for user {}:".format(user_id))
for title, rating in zip(recommended_movies, recommended_ratings):
    print(f"{title} - Estimated Rating: {rating:.2f}")
