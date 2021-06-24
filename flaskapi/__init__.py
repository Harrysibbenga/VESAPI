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

        # format the json data to get the plate number
        plate = format(data['body']['plate'])

        # url used to call the dvla api
        url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

        # format the plate to required format
        formatted_plate = "\"" + plate + "\"}"

        # set up the payload sent to the api
        payload = "{\"registrationNumber\": " + formatted_plate

        # set up request headers
        headers = {
            'x-api-key': 'IRrH9VhM8Da1Efdy7IEhwapHw2lGhVqm2EmsHDuf',
            'Content-Type': 'application/json'
        }

        # call the api
        response = requests.request("POST", url, headers=headers, data=payload)

        # return the response
        return response.text
