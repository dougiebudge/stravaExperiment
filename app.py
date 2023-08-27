# Step 1. Connect to Strava
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Auth:
    def __init__(self, client_id, client_secret, refresh_token):
        self.auth_url = "https://www.strava.com/oauth/token"
        self.payload = {
            "client_id": client_id,  # has to be in quotes
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "f": "json",
        }

    def getToken(self):
        print("Requesting Token...\n")
        res = requests.post(self.auth_url, data=self.payload, verify=False)
        access_token = res.json()["access_token"]
        print("Access Token = {}\n".format(access_token))
        return access_token


class FetchData:
    def __init__(self):
        self.ActivityURL = "https://www.strava.com/api/v3/athlete/activities"
        self.SegmentURL = "https://www.strava.com/api/v3/segments/explore"

    def FetchMeData(self, token, dataChoice):
        header = {"Authorization": "Bearer " + token}
        if dataChoice == "Segment":
            endpoint = self.SegmentURL
        elif dataChoice == "Activity":
            endpoint = self.ActivityURL
        else:
            return "Please select 'Activity' or 'Segment'"
        flag = False
        while flag == False:
            i = 1
            param = {"per_page": 200, "page": i}
            new_data = requests.get(endpoint, headers=header, params=param).json()
            if ValueError:
                flag = True
            else:
                flag = False
            if i == 1:
                my_dataset = new_data
            else:
                my_dataset.append(new_data)
            i = +1
        return my_dataset


# Step 2: Process data
class Processing:
    def __init__(self):
        pass

    def prepData(self, data):
        pass
        # drop swims
        # pick columns of interest
        # handle datetimes
        # fillnas
        # reset indexes

    def createVars(self, data):
        # generate pace and calculated fields
        # create categorical variables
        pass
