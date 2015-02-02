# Webshare-download-manager
Download manager for webshare.cz site. Flask + requests.

## Installation
`pip install webshare-download-manager`

## Config
if you have python/scripts in path:

`config_server`

else: 

`python -m appwebshare.scripts.config-script`

or manually edit config.py inside python\Lib\site-packages\appwebshare\scripts

**How to get PASSWORD?**
PASSWORD - hash generated by webshare.cz frontend:
- open webshare.cz in chrome 
- press F12 
- go to Network tab
- start recording Newtork Log
- login to webshare.cz
- find login/api request
- open Headers tab
- copy password hash


## Test server configuration
`python -m appwebshare.tests.test_webshare`


## Run server
if you have python/scripts in path: 

`run_server-script `
(may cause  Host based Intrusion Detection System exception)

or:

`python -m appwebshare.scripts.run`

or:

open run.py from python\Lib\site-packages\appwebshare\scripts


go to ([localhost:5000])

## Usage

- login with username and password set via Config
-  enter what you want to download into search
-  First .avi / .mkv / .mp4 that is smaller then SIZE(4GB default - in config.py), ordered by popularity will start downloading

