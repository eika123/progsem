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
        # use this method after *all* teams have been initialized
        self.opponents_remaining = Team.teams.copy()
        self.opponents_remaining.remove(self)
    
    def has_opponents(self):
        if self.opponents_remaining != []:
            return True
        else:
            return False
    
    def __repr__(self):
        return self.name
    
class Arena:

    arenas = []

    def __init__(self, name: str):
        self.name = name
        self.games = []
        self.arenas.append(self)

    def add_game(self, game):
        self.games.append(game)
    
    def set_games(self, games):
        self.games = games
    
    def get_games(self):
        return self.games

    def __repr__(self):
        return self.name


class Round:

    rounds = []

    def __init__(self):

        self.rounds.append(self)
        self.games = self._make_new_round()
        
        if self.games == []:
            raise ValueError('Finished setting up games, or no teams or arenas provided')


    def _make_new_round(self):
        """
        Recall! A game is an object of type Game that holds team A, team B, and the
        result between team A and team B

        @returns games: a list of games to be played this round
        """
        games = []  # list for holding the games to be played this round
        played = [] # list for holding teams that have already played this round

        # make a new list of all teams
        team_list = Team.teams.copy()

        # sort teams on how many games they are rested
        team_list.sort(key=self._sort_key_rounds_rested)
        for team in team_list:
            team.rounds_rested += 1

        # set up one game for each arena. Add teams to list played
        # to avoid double booking
        for arena in Arena.arenas:
            #print(arena.name, end=', ')

            # iterate from most rested to least rested team in team_list
            k=-1
            while k >= -len(team_list):
                team = team_list[k]
                #print(team.name, end = ' , ')
                if team.has_opponents() and team not in played:
                    played, games, opponent = self.find_opponent(team, played, games, arena)

                    if opponent:
                        # opponent found, break of out of loop
                        #k = -len(round_teams) - 1
                        break
                k -= 1
            #print('')
        #print('returning games...')
        return games

    def find_opponent(self, team, played, games, arena):
        """
        This function will find and opponent for a team. 

        input:
        --------------------------------------------------------------------------------------
        team:              the team to set up a match for
        played:            a list of opposing teams already played against
        games:             provided for bookkeeping purposes (adding opponent to games)
        team_list          neccessary??
        arena              for bookkeeping purposes when adding game
        --------------------------------------------------------------------------------------
        
        output:
        --------------------------------------------------------------------------------------
        if suitable opponent found:     played, games, opponent
        if no suitable opponent found:  played, games, None
        --------------------------------------------------------------------------------------
        """
        # sort remaining opponents according to who has most games recently rested
        team.opponents_remaining = sorted(team.opponents_remaining, reverse=True, key=self._sort_key_rounds_rested)
        for opponent in team.opponents_remaining:

            if opponent not in played and team not in played:
                #set up match
                games.append(Game(team, opponent, arena))

                # clean up

                # teams have now played each other
                team.opponents_remaining.remove(opponent)
                opponent.opponents_remaining.remove(team)

                # teams not available for further playing this round
                played.append(team)
                played.append(opponent)

                team.rounds_rested = 0
                opponent.rounds_rested = 0

                return played, games, opponent

        # traversed all remaining opponents, none matching (either team or all opponent in played)
        return played, games, None
        #raise OpponentException('no suitable opponent found for team {}'.format(team.name))
    
    def _sort_key_rounds_rested(self, team):
        return team.rounds_rested


class Game:

    games = []

    def __init__(self, team_a, team_b, arena):
        self.team_a, self.team_b = team_a, team_b
        self.arena = arena
        self.result = {self.team_a: 0, self.team_b: 0}

        
        self.games.append(self)
        arena.add_game(self)
    
    def set_result(self, score_team_a, score_team_b):
        # result = [score team_a, score team_b]
        self.result[self.team_a] = score_team_a
        self.result[self.team_b] = score_team_b



def initiate_test_data():

    #team_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    #team_names = ['alpha', 'beta', 'charlie', 'delta', 'echo', 'foxtrot']
    #team_names = ['alpha', 'beta', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel']
    team_names = ['alpha', 'beta', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima']

    """
    team_names = ['alpha', 'beta', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima', 'mike', 'november',\
        'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'whiskey', 'x-ray', 'yankee', 'zulu', 'manchester united', 'liverpool', 'arsenal']
    """
    
    """
    team_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm',\
        'n', 'o', 'p']
    """
    arena_names = ['Old Trafford', 'Wembley', 'Camp Nou']
    #arena_names = ['Old Trafford', 'Wembley', 'Camp Nou', 'Anfield']
    #arena_names = ['Old Trafford', 'Anfield', 'Wembley', 'Santiago Bernabéu', 'Camp Nou', 'Allianz Arena', 'Stamford Bridge', 'Emirates Stadium']
    for team_name in team_names:
        Team(team_name)
    
    for team_a in Team.teams:
        team_a.set_opponents()
    
    for arena_name in arena_names:
        Arena(arena_name)

    #print_opponent_lists(Team.teams)

    while True:
        try:
            #print('--------------------------')
            Round()
        except ValueError:
            done_playing = {}
            for team in Team.teams:
                if not team.has_opponents():
                    done_playing[team] = True
                else:
                    done_playing[team] = False
                    #print(team.name + " not done")
            if False in done_playing.values():
                print('error occured')
            break

    print(' ')
    print('============== checking consistencies ===============')
    print(' ')
    print('let n = len(team_names)')
    print('n(n - 1)/2 = ', len(team_names)*(len(team_names) - 1)/2)
    print('lenght og Games.games: ', len(Game.games))
    print('sum of all games in arenas', sum([len(arena.games) for arena in Arena.arenas]))
    print('=====================================================')
    print('')

def print_opponent_lists(team_list):
    for team in team_list:
        print(team.name, end=': ')
        for opponent in team.opponents_to_play:
            print(opponent.name, end=', ')
        print()

def print_rounds():
    k = 1
    print('')
    print('=='*30 + " printing tournament setup " + '=='*30 )
    print('')
    for round in Round.rounds:
        print('%3s' % (k), end=' :  |')
        for game in round.games:
            team_a = game.team_a
            team_b = game.team_b
            arena = game.arena
            print('%10s %3s %10s  @  arena: %13s' % (team_a.name, ' - ', team_b.name, arena.name), end='|      ')
            #print('[ ' + team_a.name, ' - ', team_b.name, '| arena: ', arena.name + ' ]', end=',   ')
        k += 1
        print(' ')
    print('=='*(60 + 14))



if __name__ == "__main__":

    initiate_test_data()
    #print_opponent_lists(Team.teams_with_setup)
    print_rounds()





        
        