from requests import get

BASE_URL = "https://site.api.espn.com"
TEAMS_ENDPOINT = "/apis/site/v2/sports/{sport}/{league}/teams"


def get_teams_info(sport, league):
    league_data = get(BASE_URL + TEAMS_ENDPOINT.replace("{sport}", sport).replace("{league}", league)
                      ).json()['sports'][0]['leagues'][0]

    league = league_data['name']
    league_teams = league_data['teams']

    teams_obj = {
        "League": league,
        "Teams Data": league_teams
    }
    return teams_obj
