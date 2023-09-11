import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        requesters_list = []
        requesters = json.loads(self.get_response_body())
        for requester in requesters:
            requesters_list.append(requester)
        return requesters_list
