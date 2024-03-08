from fastapi import FastAPI
import scoreboard
import team_stats
import team_info

app = FastAPI()


@app.get('/nba/games')
async def nba():
    sport = "basketball"
    league = "nba"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/collegeBasketball/mens/games')
async def mens_college_basketball():
    sport = "basketball"
    league = "mens-college-basketball"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/wnba/games')
async def wnba():
    sport = "basketball"
    league = "wnba"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/collegeBasketball/womens/games')
async def womens_college_basketball():
    sport = "basketball"
    league = "womens-college-basketball"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/nfl/games')
async def nfl():
    sport = "football"
    league = "nfl"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/nfl/team/stats/{team_query}')
async def nfl_stats(team_query: str):
    sport = "football"
    league = "nfl"
    team = team_query
    current_games = team_stats.get_overall_team_stats(sport, league, team)
    return current_games


@app.get('/collegeFootball/games')
async def mens_college_football():
    sport = "football"
    league = "college-football"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/nhl/games')
async def nhl():
    sport = "hockey"
    league = "nhl"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/mlb/games')
async def mlb():
    sport = "baseball"
    league = "mlb"
    current_games = scoreboard.get_scoreboard_data(sport, league)
    return current_games


@app.get('/teams/info/{sport_q}/{league_q}')
async def get_league_teams_info(sport_q: str, league_q: str):
    sport = sport_q
    league = league_q
    league_data = team_info.get_teams_info(sport, league)
    return league_data
