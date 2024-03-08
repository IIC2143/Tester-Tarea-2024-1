from copy import deepcopy

from src.part_1 import (
    get_all_teams,
    post_team,
    get_team,
    delete_team,
    delete_all_teams,
)

from src.part_2 import (
    get_team_matches,
    post_match,
    patch_match,
    get_matches_by_team,
)

from src.part_3 import (
    post_player,
    get_team_players,
    get_player_top_goals,
    get_player_top_assists,
    get_player_top_cards,
    get_player_from_team,
    delete_worst_team,
)

from data import TEAMS_B, MATCHES_B, PLAYERS_B


def test_3B():
    teams = deepcopy(TEAMS_B)
    matches = deepcopy(MATCHES_B)
    players = deepcopy(PLAYERS_B)

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: post_team(teams[3]),
        6: post_team(teams[4]),
        7: get_all_teams(teams),
        8: post_match(teams[1], teams[0], matches[2]),
        9: post_match(teams[1], teams[4], matches[3]),
        10: post_match(teams[2], teams[3], matches[4]),
        11: post_match(teams[2], teams[1], matches[5]),
        12: get_team_matches(teams[0]),
        13: get_team_matches(teams[1]),
        14: get_team_matches(teams[2]),
        15: post_player(teams[0], players[0]),
        16: post_player(teams[0], players[1]),
        17: post_player(teams[0], players[2]),
        18: post_player(teams[1], players[3]),
        19: post_player(teams[1], players[4]),
        20: post_player(teams[1], players[5]),
        21: post_player(teams[2], players[6]),
        22: post_player(teams[2], players[7]),
        23: post_player(teams[2], players[8]),
        24: get_team_players(teams[0]),
        25: get_team_players(teams[1]),
        26: get_player_from_team(teams[0]),
        27: get_player_from_team(teams[4]),
        28: delete_worst_team(teams, players, matches),
        29: delete_worst_team(teams, players, matches),
        30: delete_worst_team(teams, players, matches),
        31: get_all_teams(teams),
    }

    return results


if __name__ == '__main__':
    results = test_3B()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
