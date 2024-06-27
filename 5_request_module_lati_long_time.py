import requests

res = requests.get("http://api.open-notify.org/iss-now.json")
if res.status_code == 200:
    data = res.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    print(f" Latitude: {latitude},\n Longitude: {longitude},\n Timestamp: {timestamp}")
else:
    print(f"failed to get data, status code = {res.status_code}")
