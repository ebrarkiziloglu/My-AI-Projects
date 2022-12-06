import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# the dataset is taken from https://www.kaggle.com/datasets/danielgrijalvas/movies

# Load the dataset of labeled movie reviews:
data = pd.read_csv("movie_review.csv")
data = data.dropna(axis=0)

def count_reviews() -> None:    
    value_count = data["tag"].value_counts()
    print("Here are the number of positive and negative reviews in this database:")
    print(value_count)
    print("\n")
    return

# Preprocess the text data by tokenizing, removing stopwords, and stemming:
vectorizer = CountVectorizer(stop_words="english", tokenizer=lambda x: x.split(), lowercase=False)
X = vectorizer.fit_transform(data["text"])
y = data["tag"]

# Split the data into training and validation data:
train_X, validate_X, train_y, validate_y = train_test_split(X, y, random_state=1)

# Train a logistic regression model on the training data
model = LogisticRegression()
model.fit(train_X, train_y)

# Fit the model on the test data:
predict_y = model.predict(validate_X)
print("Accuracy:", accuracy_score(validate_y, predict_y), "\n")
count_reviews()

# Use the model to make predictions on new movie reviews:
new_reviews = ["I waited for so long for this movies and I had such high hopes. Yet, I didn't love it. I think it was overrated.",
                "I waited for so long for this movies and I had such high hopes. And, I loved it. I think it is not overrated.", 
                "I loved the movie!", 
                "I loved the movie.",
                "I liked the movie!",
                "I liked the movie.",
                "I LOVED IT!! BRING ME MORE!",
                "I hated the movie!",
                "I HATED THIS MOVIE!",
                "THIS MOVIE SUCKS!"]
new_X = vectorizer.transform(new_reviews)
new_predictions = model.predict(new_X)
print("Predictions:", new_predictions)
