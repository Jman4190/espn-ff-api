import pandas as pd
from static import years, position_mapping, league_teams 
import os
from dotenv import load_dotenv

load_dotenv()

draft_pick = 82 # change this to your pick

# read in CSV
new_df = pd.read_csv('league_of_geebs_drafts.csv')

# function to get adp
def get_adp(year, pick, df):
    df['year'] = df['year'].apply(str)
    adp_df = df[df['year'] == year]
    sorted_adp_df = adp_df.sort_values(by=['pick'], inplace=False)
    return sorted_adp_df[['position', 'pick']].head(pick).groupby('position').count()

# loop over all the years and create a dataframe
horizontal_concat = pd.DataFrame()
for year in years:
    filtered_df = get_adp(year, draft_pick, new_df)
    filtered_df.rename(columns = {'pick':year+'_picks'}, inplace = True)
    horizontal_concat = pd.concat([horizontal_concat, filtered_df], axis=1)
almost_final_df = horizontal_concat.fillna(0)
almost_final_df.astype(int)
print(almost_final_df)