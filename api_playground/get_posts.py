import http.client
import json
from pprint import pprint

conn = http.client.HTTPConnection("localhost", 8000)
headers_list = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}
payload = ""

conn.request("GET", "/", payload, headers_list)
response = conn.getresponse()
result_string = response.read()

# pprint(result_string.decode("utf-8"))
result_data = json.loads(result_string)
pprint(result_data)
