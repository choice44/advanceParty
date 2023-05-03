import json
import requests

response = requests.post('https://jsonplaceholder.typicode.com/posts', data={"title": "homework", "body": "chol", "userid": 1})

data = json.loads(response.text)
print(data)

with open('result.txt', 'w') as file:
    file.write(data['title']+'\n')
    file.write(data['body']+'\n')
    file.write(data['userid']+'\n')
    file.write(str(data['id'])+'\n')
