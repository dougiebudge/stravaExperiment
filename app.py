# Step 1. Connect to Strava
# Step 2. Select some interesting data stories
# Step 3. Convert to script
# Step 4. Create site in flask

# Step 1 - Connect to Strava
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"
segment_url = "https://www.strava.com/api/v3/segments/explore"

payload = {
    "client_id": "108349",
    "client_secret": "caeb9e3f1998aca26a38fb9721c6a35dd7dd548e",
    "refresh_token": "4501b6b5be686e21c33bde91f5e3074a405f06b3",
    "grant_type": "refresh_token",
    "f": "json",
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()["access_token"]
print("Access Token = {}\n".format(access_token))

# Get all my activities
header = {"Authorization": "Bearer " + access_token}

param1 = {"per_page": 200, "page": 1}
param2 = {"per_page": 200, "page": 2}
my_dataset = requests.get(activities_url, headers=header, params=param1).json()
my_dataset2 = requests.get(activities_url, headers=header, params=param2).json()
my_dataset.append(my_dataset2)

print(my_dataset[0]["name"])
print(len(my_dataset))
print(len(my_dataset2))

# Save data
with open("data.json", "w") as f:
    json.dump(my_dataset, f)
