import requests

URL = "https://httpbin.org/put"

response = requests.put(URL, stream=True)

if response.status_code == 200:
    with open('', wb) as file:
        for chunck in response.iter_content(1024):
            file.write(chunck)