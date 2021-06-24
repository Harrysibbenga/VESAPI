import requests
import os
from flask import Flask, request
# handle cors requests
from flask_cors import CORS

# handle .env files
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/", methods=['POST'])
def ves_api():
    if request.method == 'POST':

        # get data from json request
        data = request.json

        # # format the json data to get the plate number
        plate = format(data['body']['plate'])

        # url used to call the DVLA API
        url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

        # format of the body request format
        # "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"

        # set up the payload sent to the api
        payload = "{\n\t\"registrationNumber\": \"" + plate + "\n}"

        # set up request headers
        headers = {
            'x-api-key': os.getenv('REG_LOOKUP_API_KEY'),
            'Content-Type': 'application/json'
        }

        # call the api
        response = requests.request("POST", url, headers=headers, data=payload)

        # return the response
        return response.text
