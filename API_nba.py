import requests
import json
import pandas as pd
import requests as requests
from time import sleep



headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "xxx"
    }

data_game = []
data_erro = []
game = []


for item in range(6390, 7359): #range of the GAME-ID of all games from 2019/2020 season.
    try:
        #HOME TEAM STATS
        url = "https://api-nba-v1.p.rapidapi.com/gameDetails/" + str(item)
        response = requests.request("GET", url, headers=headers)
        dict_data = json.loads(response.text)

        GAME_ID = dict_data['api']['game'][0]['gameId']
        DATE = dict_data['api']['game'][0]['startTimeUTC'][:10]
        TEAM_ABBREVIATION = dict_data['api']['game'][0]['hTeam']['shortName']
        WINS = dict_data['api']['game'][0]['hTeam']['score']['win']
        LOSSES = dict_data['api']['game'][0]['hTeam']['score']['loss']
        PTS = dict_data['api']['game'][0]['hTeam']['score']['points']
        PTS_QTR1 = dict_data['api']['game'][0]['hTeam']['score']['linescore'][0]
        PTS_QTR2 = dict_data['api']['game'][0]['hTeam']['score']['linescore'][1]
        PTS_QTR3 = dict_data['api']['game'][0]['hTeam']['score']['linescore'][2]
        PTS_QTR4 = dict_data['api']['game'][0]['hTeam']['score']['linescore'][3]

        url = "https://api-nba-v1.p.rapidapi.com/statistics/games/gameId/" + str(item)
        response = requests.request("GET", url, headers=headers)
        dict_data = json.loads(response.text)

        FG_PCT = dict_data['api']['statistics'][1]['fgp']
        FT_PCT = dict_data['api']['statistics'][1]['ftp']
        FG3_PCT = dict_data['api']['statistics'][1]['tpp']
        AST = dict_data['api']['statistics'][1]['assists']
        REB = dict_data['api']['statistics'][1]['totReb']
        TOV = dict_data['api']['statistics'][1]['turnovers']
        LOC = 1
        data_game.append((GAME_ID, DATE, TEAM_ABBREVIATION, WINS, LOSSES, PTS, PTS_QTR1, PTS_QTR2, PTS_QTR3, PTS_QTR4,
                          FG_PCT, FT_PCT, FG3_PCT, AST, REB, TOV, LOC))

        #AWAY TEAM STATS
        url = "https://api-nba-v1.p.rapidapi.com/gameDetails/" + str(item)
        response = requests.request("GET", url, headers=headers)
        dict_data = json.loads(response.text)

        GAME_ID = dict_data['api']['game'][0]['gameId']
        DATE = dict_data['api']['game'][0]['startTimeUTC'][:10]
        TEAM_ABBREVIATION = dict_data['api']['game'][0]['vTeam']['shortName']
        WINS = dict_data['api']['game'][0]['vTeam']['score']['win']
        LOSSES = dict_data['api']['game'][0]['vTeam']['score']['loss']
        PTS = dict_data['api']['game'][0]['vTeam']['score']['points']
        PTS_QTR1 = dict_data['api']['game'][0]['vTeam']['score']['linescore'][0]
        PTS_QTR2 = dict_data['api']['game'][0]['vTeam']['score']['linescore'][1]
        PTS_QTR3 = dict_data['api']['game'][0]['vTeam']['score']['linescore'][2]
        PTS_QTR4 = dict_data['api']['game'][0]['vTeam']['score']['linescore'][3]

        url = "https://api-nba-v1.p.rapidapi.com/statistics/games/gameId/" + str(item)
        response = requests.request("GET", url, headers=headers)
        dict_data = json.loads(response.text)

        FG_PCT = dict_data['api']['statistics'][0]['fgp']
        FT_PCT = dict_data['api']['statistics'][0]['ftp']
        FG3_PCT = dict_data['api']['statistics'][0]['tpp']
        AST = dict_data['api']['statistics'][0]['assists']
        REB = dict_data['api']['statistics'][0]['totReb']
        TOV = dict_data['api']['statistics'][0]['turnovers']
        LOC = 0
        data_game.append((GAME_ID, DATE, TEAM_ABBREVIATION, WINS, LOSSES, PTS, PTS_QTR1, PTS_QTR2, PTS_QTR3, PTS_QTR4,
                          FG_PCT, FT_PCT, FG3_PCT, AST, REB, TOV, LOC))

        print(GAME_ID)
        sleep(4)

        df_total = pd.DataFrame(data_game,
                                columns=['GAME_ID', 'DATE', 'TEAM_ABBREVIATION', 'WINS', 'LOSSES', 'PTS', 'PTS_QTR1',
                                         'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'AST',
                                         'REB', 'TOV', 'LOC'])
        df_total.to_csv('dataset1920_total.csv')


    except:
        print(f'ERRO: {item}')
        data_erro.append(item)
        sleep(120)


df_total = pd.DataFrame(data_game, columns=['GAME_ID', 'DATE', 'TEAM_ABBREVIATION', 'WINS', 'LOSSES', 'PTS', 'PTS_QTR1', 'PTS_QTR2',
                                            'PTS_QTR3', 'PTS_QTR4', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'AST', 'REB', 'TOV', 'LOC'])
df_total.to_csv('dataset1920_total.csv')


if data_erro is not None:
    print(data_erro)
