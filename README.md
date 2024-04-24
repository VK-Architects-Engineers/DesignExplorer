# DesignExplorer

This is a modified version of design explorer to be used inside the VK / SWECO ecosystem.
You can find the open-source tool [here](https://tt-acm.github.io/DesignExplorer/)


> Design Explore is a web application to make exploring multi-dimensional design space enjoying and meaningful!

## What has been modified
Apart from some layout changes (removal of divs and source file options) we have modified how the app handles the user data file.
Essentially, the app is expecting a fileshare to exist with the data files required to have the app run.

## Setting up the server
If you're setting up this service manually on a windows machine. What you need to do is simple.
This section assumes you know what a virtual environment is, that you know how to set it up, and manipulate it.

You can copy this for ease of use
```powershell

git clone https://github.com/VK-Architects-Engineers/DesignExplorer
# create a virtualenvironment
cd DesignExplorer
py -m virtualenv venv
./venv/scripts/activate
pip install -r requirements.txt
# I prefer you'd run this using waitress and not flask, for generallity's sake, the app is setup to run as such
python app.py
```
## Datastore
This server EXPECTS a datastore server to exist that can send images/json and csv data to the client. This datastore has to serve this content over http requests. It could also be that CORS has to be enabled to properly run this, but in the current stage that might not be necesarry.

## URL queries
The tool has support for a single URL query `document`.
By passing a string value with this query parameter, you can directly load a stored document in the datastore.\
**Usage**\
`http://serverurl/DesignExplorer?document=examplename`
will open the `data.csv` file that is placed on
`http://datastore/designexplorer_data/examplename/data.csv`


## Environment variables
There are 2 environemnt variables available for your consideration. These are optional, but can be usefull in debugging a local debug server
```ini
DOCUMENT_DATA_HOST="http://example.datastore.com"
DOCUMENT_DATA_URI="designexplorer_data"
```
You can use a file called `.env` and place it in the project root. Or set them up in your terminal's environment

`DOCUMENT_DATA_HOST` : this configures the server to go and find 'data files' on the specified server, this server needs to be accessible to designexplorer

`DOCUMENT_DATA_URI` : the second part of the datastore, the path on the datastore to the folder that contains the actual data. Note, the only valid source for datasource files is a datasource that can deliver files over http. 
(a nginx server serving static files works too)

Populating the datastore is the responsibility of a different entity

## Todo
- Make sure that data in the datastore can only contain image, json and csv files
- Prettify logos
- Get rid of 'required' default data, or place it inside repo and have it accessed from there.
- Get rid of excpetion y_axis that occurs when directly heading to a document using ?document=
- set up CORS


## Design Explorer is built on top of these plugins and web technologies:
### [Bootstrap template with side bar](http://getbootstrap.com/)
### [D3 Parallel coordinates](https://syntagmatic.github.io/parallel-coordinates/)
### [D3js](http://d3js.org/)
### [Ion.Range Slider](http://ionden.com/a/plugins/ion.rangeSlider/en.html)
### [jQuery Star Rating Plugin](http://www.fyneworks.com/jquery/star-rating/)
### [Pace](http://github.hubspot.com/pace/docs/welcome/)
### [Radar Chart](https://github.com/alangrafu/radar-chart-d3)
### [Spectacles](https://github.com/tt-acm/Spectacles.WebViewer) - 3D viewer
### [Scatter-matrix Chart](https://github.com/benjiec/scatter-matrix)

### [Flask](https://flask.palletsprojects.com/en/3.0.x/)