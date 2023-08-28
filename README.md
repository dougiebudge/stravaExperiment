This repo is for me to explore the returns from the acitivities Strava API endpoint.

There are two Strava endpoints that offer interesting data; segments and activities. 
Segments lists Strava segments in a specfic longlat area which would be great for some kind of explorer app but some segment information is behind a paywall. Most useful activity data is available for non-paying users via the activities endpoint so I'm having a play with that first.

### App.py ###
This file has an Auth and a FetchData class that generate an auth token before making a GET request to Strava a dataset for activity or segment data.

### Explore.ipynb ###
This notebook visualises and analyses my acitivity data and trains some ML predictors. 
General findings are that Distance, Elevation per KM and distance covered the month prior to exercise all have some degree of feature importance. 

