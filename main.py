import json
from app import Auth, FetchData
from configparser import ConfigParser
import pandas as pd

# Pull in my account IDs
config = ConfigParser()
config.read("creds.ini")
client_id = config.get("tokens", "client_id")
client_secret = config.get("tokens", "client_secret")
refresh_token = config.get("tokens", "refresh_token")

# Generate my auth token
auth = Auth(client_id, client_secret, refresh_token)
token = auth.getToken()

# Get my activity data using the auth token generated
fetch = FetchData()
data = fetch.FetchMeData(token)

# Save data
# with open("data.json", "w") as f:
#   json.dump(data, f)

print(len(data))
