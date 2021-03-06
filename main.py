import uvicorn
from fastapi import FastAPI
import pickle
import os
import pandas as pd
import numpy as np
from pydantic import BaseModel
from RecommendationSystems import RecommendationSystem


app = FastAPI()


# Load model
pickle_file_open = open("recommendation.pkl","rb") # open pickle file in read mode
model = pickle.load(pickle_file_open) # to load the pickle file

# loading dataset with userId
ratings = pd.read_csv("ratings_small.csv")


@app.get('/')
def home():
    return "Welcome! Add /docs in the url and input these values in the Post method: userId=1, movieId=302, rating=3"

# @app.get("/{name}")
# def get_name(name: str):
#     return {"Welcome,":f"{name}"}


@app.post('/predict')
def predict_rating(data:RecommendationSystem):
    data = data.dict()
    # print(data)
    userId = data['userId']
    movieId = data['movieId']
    rating = data['rating']
    print(model.predict(userId,movieId,rating))
    result = model.predict(userId,movieId,rating)[3]
    return (f"The predicted rating is {result}")
    # print(result)


if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=5000)