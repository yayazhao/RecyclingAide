
from urllib.parse import urlencode
import requests
import pandas as pd

api_key='AIzaSyA3IL6n1GRc5dWai6m53fHe4k818Cgf2OA'

def extract_lat_lng(address_or_postalcode, data_type='json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get('lng')

def get_lat_ln():
    df = pd.read_csv('SW_FacilityList.csv')
    df['lat'] = 0.0
    df['lng'] = 0.0
    nRows, nCols = df.shape
    for row in range(nRows):
        addr = f"{df.iloc[row]['Address']}, {df.iloc[row]['City']}, NC"
        lat, lng = extract_lat_lng(addr)
        df.loc[row, "lat"] = lat
        df.loc[row, "lng"] = lng
    df.to_csv('SW_FacilityList_LatLng.csv')

get_lat_ln()