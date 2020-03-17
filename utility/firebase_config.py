import google
import requests
from flask import json
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


class Configuration:

    def __init__(self):
        self.database_base_url = "https://one-star-reviews-1553143808077.firebaseio.com"
        self.auth_json = "/Users/victorious/OneStarReview/files/firebase_auth.json"
        self.scopes = [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/firebase.database"
        ]
        self.credentials = service_account.Credentials.from_service_account_file(
        self.auth_json, scopes=self.scopes)

        # Create auth Session
        self.authed_session = AuthorizedSession(self.credentials)
        self.response = self.authed_session.get(self.database_base_url)
        self.request = google.auth.transport.requests.Request()

        # Set Access Token for subsequent access to Firebase DB
        self.credentials.refresh(self.request)
        self.access_token = self.credentials.token

        # Database values
        self.version = ""
        self.id = "/"

    def get_request(self, version):
        self.version = version
        url_params = ".json?access_token=" + self.access_token
        response = requests.get(self.database_base_url + self.version + url_params)
        return json.loads(response.text)

    def post_request(self):
        json_object = {"key": "value"}
        url_params = ".json?access_token=" + self.access_token
        response = requests.post((self.database_base_url + self.version + self.id + str(id) + url_params), json.dumps(json_object))
        return json.loads(response.text)

    def put_request(self, version, update_object):
        self.version = version

        # THIS WILL OVERRIDE ENTIRE JSON IN DB!

        url_params = ".json?access_token=" + self.access_token
        # print(self.database_base_url + self.version + url_params)
        response = requests.put((self.database_base_url + self.version + url_params), json.dumps(update_object))
        return json.loads(response.text)
