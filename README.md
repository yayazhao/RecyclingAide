# RecyclingAide

## Overview
Our goal for this project is to make people easy to view, and navigate to nearby waste facilities. 
1. The dataset used here is solid waste facilities, which is obtained from <a href="https://deq.nc.gov/about/divisions/waste-management/sw/data/facility-lists"><b>NC DEQ</b></a>
2. The Flask framework was used to build the website, the Flask-Restful was used to provide data services, the Kendo UI for jQuery was for front end development, and Google Maps was used to provide the map services.
3. GitHub is used to host <a href="https://github.com/yayazhao/RecyclingAide"><b>our code</b></a>, Heroku to host our website, and JetBrains PyCharm as the IDE to do development. <a href="https://recycling-aide.herokuapp.com"><b>Here</b></a> can access to our website hosted at Heroku.

## Run locally
1. Clone or download code to a folder on your local machine
2. Go to that folder
3. Register with Google Maps services and create an API Key. Then open template/site.html, find the line which starts with ```src="https://maps.googleapis.com/maps/api/js?key=```, and replace the key value with your key.
3. Run the below commands:
   ```buildoutcfg
   pip install -r requirements.txt
   flask run
   ```
   You should see something including the below:
   ```buildoutcfg
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```