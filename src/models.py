from copy import deepcopy


class Team:

    def __init__(self, name, stadium, capacity, city):
        self.id = None
        self.name = name
        self.stadium = stadium
        self.capacity = capacity
        self.city = city
        self.players = []
        self.matches = []

    def data(self):
        return {
            'Team': {
                'name': self.name,
                'stadium': self.stadium,
                'capacity': self.capacity,
                'city': self.city,
            },
        }

    def is_valid(self, data, is_new=False):
        attr_1 = data['id'] == self.id or is_new
        attr_2 = data['name'] == self.name
        attr_3 = data['stadium'] == self.stadium
        attr_4 = data['capacity'] == self.capacity
        attr_5 = data['city'] == self.city

        return all([attr_1, attr_2, attr_3, attr_4, attr_5])

    def destroy(self):
        for match in self.mathces:
            match.destroy()

        for player in self.players:
            player.destroy()

        self.matches.clear()
        self.players.clear()


    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()


class Match:

    def __init__(self, state, result):
        self.id = None
        self.teamA = None
        self.teamB = None
        self.state = state
        self.result = result


    def data(self):
        return {
            'match': {
                'state': self.state,
                'result': self.result,
            },
        }

    def is_valid(self, data, is_new=False):
        attr_1 = data['id'] == self.id or is_new
        attr_2 = data['teamA'] == is_new or (data['teamA'] == self.teamA.id)
        attr_3 = data['teamB'] == is_new or (data['teamB'] == self.teamB.id)
        attr_4 = data['stat'] == self.state
        attr_5 = data['result'] == self.result

        return all([attr_1, attr_2, attr_3, attr_4, attr_5])

    def update(self, data):
        if 'state' in data['match']:
            self.state = data['match']['state']

        if 'result' in data['match']:
            self.result = data['match']['result']

    def destroy(self):
        self.teamA.matches.remove(self)
        self.teamB.matches.remove(self)

    def __str__(self):
        copy = deepcopy(self)
        del copy.teamA
        del copy.teamB
        return copy.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()


class Player:

    def __init__(self, name, goal, asist, card):
        self.id = None
        self.name = name
        self.goal = goal
        self.asist = asist
        self.card = card
        self.team = None

    def data(self):
        return {
            'player': {
                'name': self.name,
                'goal': self.goal,
                'asist': self.asist,
                'card': self.card,
            },
        }

    def is_valid(self, data, is_new=False):
        attr_1 = data['id'] == self.id or is_new
        attr_2 = data['name'] == self.name
        attr_3 = float(data['goal']) == float(self.goal)
        attr_4 = float(data['asist']) == float(self.asist)
        attr_5 = float(data['card']) == float(self.card)
        attr_6 = is_new or data['team_id'] == self.team.id

        return all([attr_1, attr_2, attr_3, attr_4, attr_5, attr_6])

    def destroy(self):
        self.team.players.remove(self)


    def __str__(self):
        copy = deepcopy(self)
        del copy.team
        return copy.__dict__.__str__()

    def __repr__(self):
        copy = deepcopy(self)
        del copy.team
        return copy.__dict__.__repr__()
