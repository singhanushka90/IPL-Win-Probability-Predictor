import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel , computed_field, Field 
from typing import Annotated , Literal
import pickle

app=FastAPI()
best_rf=pickle.load(open("ipl_model.pkl","rb"))
trf=pickle.load(open("ipl_transformer.pkl","rb"))

class ChatRequest(BaseModel):
    batting_team:Annotated[Literal['Sunrisers Hyderabad','Mumbai Indians', 'Royal Challengers Bangalore','Kolkata Knight Riders', 'Kings XI Punjab','Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals'],Field(description="Select the batting team")]
    bowling_team:Annotated[Literal['Sunrisers Hyderabad','Mumbai Indians', 'Royal Challengers Bangalore','Kolkata Knight Riders', 'Kings XI Punjab','Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals'],Field(description="Select the bowling team")]
    city:Annotated[str,Field(description="Enter Match city")]
    runs_left:Annotated[int,Field(gt=0,description="Runs needed to win")]
    ball_left:Annotated[int,Field(gt=0,description="Balls Remaining")]
    wickets_left:Annotated[int,Field(ge=0,le=10,description="Wickets in hand")]
    total_runs_x:Annotated[int,Field(gt=0,description="Target Score")]
    current_score:Annotated[int,Field(gt=0,description="enter current score")]



    @computed_field
    def crr(self)->float:
        return (self.current_score*6)/(120-self.ball_left)
    
    @computed_field
    def rrr(self)->float:
        return (self.runs_left*6)/self.ball_left
    

@app.get("/home")
def home():
    return {"status": "Healthy",
           "service": "IPL-Predictor-API",
           "version": "1.0.0",
           "model_loaded": True,
           "transformer_loaded": True}

@app.post("/predict")
def predict(data:ChatRequest):
    features=pd.DataFrame({
        "batting_team":[data.batting_team],
        "bowling_team":[data.bowling_team],
        "city":[data.city],
        "runs_left":[data.runs_left],
        "ball_left":[data.ball_left],
        "wickets_left":[data.wickets_left],
        "total_runs_x":[data.total_runs_x],
        "current_score":[data.current_score],
        "crr":[data.crr],
        "rrr":[data.rrr]
    })

    transformed_data=trf.transform(features)
    prediction=best_rf.predict_proba(transformed_data)
    batting_win=round(prediction[0][1]*100,2)
    bowling_win=round(prediction[0][0]*100,2)
    return {"batting_team":data.batting_team,
            "bowling_team":data.bowling_team,
            "batting_win_probability":f"{batting_win}%",
            "bowling_win_probability":f"{bowling_win}%"}

