import random
import pokemon

# make a team of six pokemon:
def Generate_Team(trainer, team_name):

    team_name = str('team ' + team_name)
    team = []
    poke_counter = 6

    #get file of names
    with open('names.txt', 'r') as f:
        names = f.read().split(' ')
        del names[-1]

    while poke_counter > 0:
        poke_name = names[random.randint(0,len(names) - 1)]
        poke = pokemon.Pokemon(poke_name)
        team.append(poke)
        poke_counter -= 1
    return team
