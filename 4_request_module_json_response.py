import requests
res=requests.get("http://api.open-notify.org/iss-now.json")
if res.status_code==200:
    print(res.json())
else:
    print(f"failed to get data ,status code = {res.status_code}")
