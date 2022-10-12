import requests
import time
from requests.adapters import HTTPAdapter

class RequestLogger(HTTPAdapter):

    def __init__(self, *args, **kwargs):
        super(RequestLogger, self).__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        self.start_time = time.time()
        return super(RequestLogger, self).send(request, **kwargs)

    def build_response(self, *args):
        resp = super(RequestLogger, self).build_response(*args)
        latency = time.time() - self.start_time
        print(f"url={resp.url} method={resp.request.method} status={resp.status_code} latency={latency}")
        return resp
        

s = requests.Session()
s.mount('https://', RequestLogger())

r = s.get('https://github.com')
print("HTTP Response: ", r.status_code)

