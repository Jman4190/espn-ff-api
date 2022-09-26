import requests
import pandas as pd
from espn_api import get_draft_details, get_player_info, get_team_info
from static import years, position_mapping, league_teams 
import os
from dotenv import load_dotenv

load_dotenv()

# load in environment variables
LEAGUE_ID = os.getenv('LEAGUE_ID')
SWID_COOKIE = os.getenv('SWID_COOKIE')
ESPN_S2_COOKIES = os.getenv('ESPN_S2_COOKIES')

# update this to use env variables
espn_cookies = {"swid": SWID_COOKIE,
                "espn_s2": ESPN_S2_COOKIES}


# create an empty dataframe to append to
all_drafts_df = pd.DataFrame()

# loop over all the years
for year in years:
    print(year)
    # get all needed info for the year
    draft_df = get_draft_details(LEAGUE_ID, year, espn_cookies)
    player_df = get_player_info(year, espn_cookies)
    team_df = get_team_info(year)
    # merge tables together
    df2 = pd.merge(draft_df, player_df, how="inner", left_on="playerId", right_on = "player_id")
    final_df = pd.merge(df2, team_df, how="inner", left_on="proTeamId", right_on = "team_id")
    # rename columns and map values for easier consumption
    league_draft = final_df.replace({"defaultPositionId": position_mapping})
    league_draft_info = league_draft.replace({"teamId": league_teams})
    league_draft_final = league_draft_info[['overallPickNumber', 'teamId', 'defaultPositionId', 'fullName', 'team name']]
    league_draft_final.rename(columns = {'overallPickNumber':'pick', 'teamId':'geebs_team',
                              'defaultPositionId':'position', 'fullName':'player', 'team name': 'player_team'}, inplace = True)
    league_draft_final['year'] = year
    league_draft_final['year'] = league_draft_final['year'].apply(str)
    all_drafts_df = all_drafts_df.append(league_draft_final)

# export into CSV
all_drafts_df.to_csv('your_draft_results_file.csv', index=False)