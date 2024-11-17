import os
import json
import src
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
# from mangum import Mangum



app = FastAPI()
# handler = Mangum(app)

    
@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/return_nearby_charging_stations/")
async def return_nearby_charging_stations(lat: float, long: float, count: int = 5):
    nearby_stations = src.return_nearby_stations(lat, long, count)
    return {"stations": nearby_stations}
    

@app.get("/post_waypoints/")
async def post_waypoints(waypoints, count: int = 5):
    all_waypoints = waypoints
    updated_waypoints, station_indexes, recharge_goal, price_list= src.get_all_stations_along_route(waypoints, count)
    """
    updated_waypoints- array of sequential waypoints (where some waypoints are substituted for charging stations) to create a new route with
    station_indexes- the indexes of the stations in updated_waypoints 
    recharge_goal- the amount to recharge to at each station
    price_list- the estimated price of each recharge at each station
    """
    return {"updated_waypoints": updated_waypoints, "station_indexes": station_indexes, "recharge_goal": recharge_goal, "price_list": price_list}

