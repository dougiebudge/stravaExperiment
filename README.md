This repo is for me to explore the returns from the acitivities Strava API.

Strava offers two endpoints with interesting data; segments and activities. 
Segments lists Strava segments in a specfic longlat area which would be great for some kind of explorer app but some segment information is behind a paywall and I'm using my free account for access. Most useful activity data is available for non-paying users via the activities endpoint so I'm having a play with that first.

### App.py ###
This file has an Auth and a FetchData class. Auth generates an auth token for use by FetchData which makes a GET request to Strava - fetching all available data for activities.

### Explore.ipynb ###
This notebook visualises and analyses my acitivity data and trains some ML predictors. 
General findings are that Distance, Elevation per KM and distance covered the month prior to exercise all have some degree of feature importance. 

