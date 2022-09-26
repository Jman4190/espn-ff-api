# espn-ff-api
How to Access the Unofficial ESPN Fantasy Footbball API with Python

[Link to Blog Post](https://jman4190.medium.com/how-to-use-python-with-the-espn-fantasy-draft-api-ecde38621b1b) 

## Requirements
- pandas
- requests
- espn fantasy football account
- python-dotenv

## Storing Environment Variables
Create a `.env` file and add the following
```
export LEAGUE_ID = 'YOU_LEAGUE_ID_HERE'
export SWID_COOKIE = "YOUR_SWID_COOKIE_HERE"
export ESPN_S2_COOKIES = "YOUR_ESPN_S2_COOKIE_HERE"
```
## Modifying Variables
Make sure to update your league_id and adjust the years list in `static.py` to match the years in your fantasy football league

## Running the script
```
$ python draft_history.py
```
