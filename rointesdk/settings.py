"""Configuration constants"""

AUTH_HOST = "https://www.googleapis.com"
AUTH_VERIFY_URL = "/identitytoolkit/v3/relyingparty/verifyPassword"
AUTH_ACCT_INFO_URL = "/identitytoolkit/v3/relyingparty/getAccountInfo"
AUTH_TIMEOUT_SECONDS = 15

AUTH_REFRESH_ENDPOINT = "https://securetoken.googleapis.com/v1/token"

FIREBASE_APP_KEY = "AIzaSyDfqBq3AfIg1wPjuHse3eiXqeDIxnhvp6U"
FIREBASE_DEFAULT_URL = "https://oem2-elife-cloud-prod-default-rtdb.firebaseio.com"
FIREBASE_INSTALLATIONS_PATH = "/installations2.json"
FIREBASE_DEVICES_PATH_BY_ID = "/devices/{}.json"
FIREBASE_DEVICE_DATA_PATH_BY_ID = "/devices/{}/data.json"
FIREBASE_DEVICE_ENERGY_PATH_BY_ID = "/history_statistics/{}/daily/"

ENERGY_STATS_MAX_TRIES = 5
