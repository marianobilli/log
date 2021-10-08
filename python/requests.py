
import requests
import urllib3

urllib3.disable_warnings()

request_session = requests.Session()
retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
request_session.mount('https://', HTTPAdapter(max_retries=retries))

api_url = "https://localhost:9000/hello/status" 
response = request_session.get(api_url, verify=False)
assert response.status_code == 200
