import time
import requests
import pandas as pd


def fetch_iss_data():
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        latitude = (data['iss_position']['latitude'])
        longitude = (data['iss_position']['longitude'])
        timestamp = data['timestamp']
        return {'timestamp': timestamp, 'latitude': latitude, 'longitude': longitude}
    else:
        print(f"Failed to fetch data, status code: {res.status_code}")
        return None


def main():
    records_needed = 1
    records_collected = 0
    iss_data = []

    while records_collected < records_needed:
        try:
            data = fetch_iss_data()
            if data:
                iss_data.append(data)
                records_collected += 1
            time.sleep(1)
            print(data)
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            time.sleep(5)

    df = pd.DataFrame(iss_data)
    csv_filename = 'iss_location_data.csv'
    df.to_csv(csv_filename, index=False)

    print(f"Successfully wrote {records_needed} records to {csv_filename}")


main()
