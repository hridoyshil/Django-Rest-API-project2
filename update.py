import requests
import json

URL = "http://127.0.0.1:8000/aicreate/"

data = {
    "id": 1,
    "teacher_name": "Sagor Shil",
    "course_name": "EEE",
}

json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data = r.json()
print(data)
