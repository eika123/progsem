from typing import List

class OpponentException(Exception):

    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors

    def __init__(self, message):
        super().__init__(message)
    
    

class Team:

    teams = []

    def __init__(self, name: str):

        self.opponents_remaining = []
        self.name = name
        self.rounds_rested = 0

        self.teams.append(self)
    
    def set_opponents(self):
        self.opponents_remaining = Team.teams.copy()
        self.opponents_remaining.remove(self)
    
    def has_opponents(self):
        if self.opponents_remaining != []:
            return True
        else:
            return False
    
class Arena:

    arenas = []

    def __init__(self, name):
        self.name = name
        self.games = []
        self.arenas.append(self)

    def add_game(self, game):
        self.games.append(game)
    
    def set_games(self, games):
        self.games = games


class Round:

    rounds = []

    def __init__(self):

        self.rounds.append(self)
        self.games = self._make_new_round()
        
        if self.games == []:
            raise ValueError('Finished setting up games, or no teams or arenas provided')

    def find_opponent(self, team, played, games, round_teams, arena):
        print('finding matches...')
        for opponent in team.opponents_remaining.sort(reverse=True,\
            key=self._sort_key_rounds_rested):
            # match!
            if opponent not in played and team not in played:
                #set up match
                games.append(Game(team, opponent, arena))
                # clean up
                team.opponents_remaining.remove(opponent)
                opponent.opponents_remaining.remove(team)

                played.append(team)
                played.append(opponent)

                round_teams.remove(team)
                round_teams.remove(opponent)

                team.rounds_rested = 0
                opponent.rounds_rested = 0

                print("set up game and cleaned up...")
                return played, games, opponent
        return played, games, None
        #raise OpponentException('no suitable opponent found for team {}'.format(team.name))
    
    def _sort_key_rounds_rested(self, team):
        return team.rounds_rested

    def _make_new_round(self):
        games = []
        played = [] # already played this round

        round_teams = Team.teams.copy()

        # sort teams on how many games they are rested
        round_teams.sort(key=self._sort_key_rounds_rested)
        for team in round_teams:
            team.rounds_rested += 1

        # set up one game for each arena. Add teams to list played
        # to avoid double booking
        for arena in Arena.arenas:
            print(arena.name, end=', ')

            k=-1
            while k >= -len(round_teams):
                team = round_teams[k]
                print(team.name, end = ' , ')
                if team.has_opponents() and team not in played:
                    played, games, opponent = self.find_opponent(team, played, games, round_teams, arena)

                    if opponent:
                        # break of out of loop
                        k = -len(round_teams) - 1
                k -= 1
            print('')
        print('returning games...')
        return games

class Game:

    games = []

    def __init__(self, team_a, team_b, arena):
        self.team_a, self.team_b = team_a, team_b
        self.arena = arena
        self.result = {team_a: 0, team_b: 0}

        
        self.games.append(self)
        arena.add_game(self)
    
    def set_result(self, score_team_a, score_team_b):
        # result = [score team_a, score team_b]
        self.result[self.team_a] = score_team_a
        self.result[self.team_b] = score_team_b



def initiate_test_data():

    #team_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    team_names = ['a', 'b', 'c', 'd', 'e', 'f']
    team_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    """
    team_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm',\
        'n', 'o', 'p']
    """
    #arena_names = ['Old Trafford', 'Wembley', 'Camp Nou', 'Anfield']
    arena_names = ['Old Trafford', 'Anfield', 'Wembley']
    for team_name in team_names:
        Team(team_name)
    
    for team_a in Team.teams:
        team_a.set_opponents()
    
    for arena_name in arena_names:
        Arena(arena_name)

    #print_opponent_lists(Team.teams)

    while True:
        try:
            print('--------------------------')
            Round()
        except ValueError:
            done_playing = {}
            for team in Team.teams:
                if not team.has_opponents():
                    done_playing[team] = True
                else:
                    done_playing[team] = False
                    print(team.name + " not done")
            if False in done_playing.values():
                print('error occured')
            break

    print(' ')
    print('============== checking consistencies ===============')
    print(' ')
    print(len(team_names)*(len(team_names) - 1)/2)
    print('lenght og Games.games: ', len(Game.games))
    print('sum of all games in arenas', sum([len(arena.games) for arena in Arena.arenas]))

def print_opponent_lists(team_list):
    for team in team_list:
        print(team.name, end=': ')
        for opponent in team.opponents_to_play:
            print(opponent.name, end=', ')
        print()

def print_rounds():
    k = 1
    for round in Round.rounds:
        print(k, end=' : ')
        for game in round.games:
            team_a = game.team_a
            team_b = game.team_b
            arena = game.arena

            print('[ ' + team_a.name, ' - ', team_b.name, '| arena: ', arena.name + ' ]', end=',   ')
        k += 1
        print(' ')



if __name__ == "__main__":

    initiate_test_data()
    #print_opponent_lists(Team.teams_with_setup)
    print_rounds()





        
        