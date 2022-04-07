from pickle import GET
from fastapi import FastAPI
import asyncio
app = FastAPI()
import requests
from requests.structures import CaseInsensitiveDict

    #From here to the next indented comment is the authorization header, you can just copy paste it while using the LongMetal team API
url = "https://info.firstinspires.org/e2t/tc/VVNLPL1Ch1DRW4lbqC473BhZLW2C4PM94lvDgFN4Hzmfm3p_97V1-WJV7CgQ_0W1DpDQd4r9SgRN349X2Jz4k27W6v_V9X4yTfVFN33N18y_gZ3pW6J2BL55Tmn4KN15z1FYz7w2TW3zfdxL7P35VPW1yTj4V7bBfmYW8CTjTL3VLcsQW8WcZct6-v4rtW7ntY-t97qTpKW8_x0cP2GyK61W7hhKdG6rWKBcW7Jsn_N5zGB9SW1K_l3M4MySxyW4jG70Q1g6c0bW8x20yd4yHMGXW4CDQd56-5sqkVy00xj34xdzhW8mpN0X6SwWL2W91Dwjy8VK9-MV6ZVcC4Vj9bjW9j_KC04Lm1CMW3tp28z5ZsyH63nxV1"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Basic YTNkd2FmbGU6M2E5ZWQ1OWUtZjA0ZS00MWFjLTlkNDUtZTJjNmQ2MjgzODIz"
resp = requests.get(url, headers=headers)
print(resp.status_code)
    #The Response code should be 200, if not follow the table in the documentation

#This is a call for seasonal data
url = "https://frc-api.firstinspires.org/v2.0/2020"

payload={}
headers = {
  'Authorization': 'Basic <credentials>',
  'If-Modified-Since': ''
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
async def root():
    return {"Oinga Boinga"}
    