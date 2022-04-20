import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime


st.title("Paradise Bus Tracker")


url = "https://api.transloc.com/feeds/3/vehicle_statuses?include_arrivals=true&agencies=112&arrival_stop=4115942&schedules=true"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)

output = response.json()

Timestamp = output['arrivals'][0]["timestamp"]
print(datetime.utcnow().timestamp())


# print(pos)

# # st.map(pos)
# # st.map(output['vehicles'][-1]["position"])

# df = pd.DataFrame(
#      [pos],
#      columns=['lat', 'lon'])

# st.map(df)

# how far is the bus from the user?
"""
Processing timestamps for arrival times
"""
# Bus Stop ID: 4115942
# Bus Stop Name: "Courtney RD"
# Bus Stop Latitude: 37.76498
# Bus Stop Longitude: -122.44897

st.info("The next bus is in " + str(int(datetime.fromtimestamp(Timestamp).strftime("%M")) - int(datetime.utcnow().strftime("%M"))) + " minutes")
