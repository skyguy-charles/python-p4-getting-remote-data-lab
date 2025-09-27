import urllib.request
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = urllib.request.urlopen(self.url)
        return response.read()

    def load_json(self):
        body = self.get_response_body()
        return json.loads(body)
