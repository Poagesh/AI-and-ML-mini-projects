# Movie Recommendation System

This project implements a movie recommendation system using collaborative filtering based on K-Nearest Neighbors (KNN). The system is built with the `Surprise` library, which is designed for building and evaluating recommender systems. It uses the MovieLens 100k dataset and generates personalized movie recommendations for users based on their preferences.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Algorithm](#algorithm)
- [Contributing](#contributing)
- [License](#license)

## Overview

This recommendation system makes personalized movie suggestions by analyzing the historical ratings of users. The recommendations are generated using collaborative filtering, where users' preferences are used to predict ratings for movies they haven't seen.

## Features

- Loads the MovieLens 100k dataset using `Surprise`.
- Trains a recommendation model based on the K-Nearest Neighbors (KNN) algorithm.
- Makes movie recommendations for users based on their previous ratings.
- Displays estimated ratings for recommended movies.

## Installation

To run the project, ensure you have Python 3.x installed along with the following libraries:

```bash
pip install pandas scikit-surprise numpy opencv-python-headless
```

Additional packages include:
- `pandas` for handling data frames and manipulating the movie dataset.
- `scikit-surprise` for implementing the collaborative filtering algorithm.
- `numpy` for numerical computations.

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Run the script**:

   The script prompts you for a user ID, generates movie recommendations for that user, and prints the top recommended movies along with their estimated ratings.

   ```bash
   python recommend.py
   ```

3. **Input the user ID**:

   When the script runs, input the user ID to get personalized recommendations.

   Example:

   ```
   Enter your User ID: 196
   Recommended movies for user 196:
   Star Wars (1977) - Estimated Rating: 4.80
   Contact (1997) - Estimated Rating: 4.50
   ... (other movies)
   ```

## Dataset

The MovieLens 100k dataset is used in this project. It contains 100,000 ratings from 943 users on 1682 movies. The dataset is available directly from the `surprise` library.

- **Movie Details**: Titles and movie IDs are extracted from the MovieLens dataset using the file `u.item`.

## Algorithm

The recommendation system is built using **collaborative filtering** based on the KNN algorithm:

- **KNN (K-Nearest Neighbors)**: Predicts movie ratings for a user by analyzing similar users (users who have rated the same movies similarly).
- **User-based Filtering**: The system finds users with similar tastes to the active user and predicts the active user's rating for a movie based on those users' ratings.

### Model Training

1. The MovieLens dataset is loaded using `Surprise`.
2. The dataset is split into training and testing sets (75% train, 25% test).
3. The KNN model is trained using user-based filtering.
4. The model's performance is evaluated using Root Mean Squared Error (RMSE).

## Example Output

```
Enter your User ID: 196
Recommended movies for user 196:
1. Star Wars (1977) - Estimated Rating: 4.80
2. Contact (1997) - Estimated Rating: 4.50
3. Fargo (1996) - Estimated Rating: 4.47
4. L.A. Confidential (1997) - Estimated Rating: 4.45
5. Titanic (1997) - Estimated Rating: 4.44
```

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.
