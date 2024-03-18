from copy import deepcopy

from src.part_1 import (
    get_all_teams,
    post_team,
    get_team,
    delete_team,
    delete_all_teams,
)

from data import TEAMS_C, WRONG_TEAMS_2


def test_1C():
    teams = deepcopy(TEAMS_C[0:3])
    bad_teams = deepcopy(WRONG_TEAMS_2[0:3])

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: not post_team(bad_teams[0]),
        6: not post_team(bad_teams[1]),
        7: not post_team(bad_teams[2]),
        8: get_all_teams(teams),
        9: get_team(teams[0]),
        10: get_team(teams[1]),
        11: not get_team(bad_teams[0]),
        12: delete_team(teams, teams[0]),
        13: delete_team(teams, teams[1]),
        14: not delete_team(teams, bad_teams[0]),
        15: get_all_teams(teams),
        16: not post_team(bad_teams[0]),
        17: not post_team(bad_teams[1]),
    }

    return results


if __name__ == '__main__':
    results = test_1C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
