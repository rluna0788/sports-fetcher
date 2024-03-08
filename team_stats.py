from requests import get

BASE_URL = "https://site.api.espn.com"
SINGLE_TEAM_ENDPOINT = "/apis/site/v2/sports/{sport}/{league}/teams/"  # append team abbreviation


def get_overall_team_stats(sport, league, team):
    team_data = get(BASE_URL + SINGLE_TEAM_ENDPOINT.replace("{sport}", sport).replace("{league}", league)
                    + team).json()['team']

    team_name = team_data['displayName']
    team_abbreviation = team_data['abbreviation']

    for item in team_data['record']['items']:
        if item['type'] == "total":
            team_stats = item['stats']

    team_obj = {
        "Team": team_name,
        "Abbreviation": team_abbreviation,
        "Statistics": team_stats
    }
    return team_obj
