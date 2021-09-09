import requests
import json

host_url = "http://localhost:3000/posts"

response_code = requests.get(host_url)
print(response_code)

respose_result = (json.dumps(response_code.json(),indent=4))
print(respose_result)