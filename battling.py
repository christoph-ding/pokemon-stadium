import random # is this neccesary?

# engine for determining combat math
def Calculate_Dp(attacker_atk, attacker_type, defender_def, defender_type):

    type_table = {'normal': {'normal': 1, 'fire': 1 , 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                             'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 0,
                             'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1},
                  'fire': {'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 1, 'grass': 2, 'ice': 2, 'fighting': 1,
                           'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 2, 'rock': 0.5, 'ghost': 1,
                           'dragon': 0.5, 'dark': 1, 'steel': 2, 'fairy': 1},
                  'water': {'normal': 1, 'fire': 2, 'water': 0.5, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                            'poison': 1, 'ground': 2, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1,
                            'dragon': 0.5, 'dark': 1, 'steel': 1, 'fairy': 1},
                  'electric': {'normal': 1, 'fire': 1, 'water': 2, 'electric': 0.5, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                               'poison': 1, 'ground': 0, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                               'dragon': 0.5, 'dark': 1, 'steel': 1, 'fairy': 1},
                  'grass': {'normal': 1, 'fire': 0.5, 'water': 2, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                            'poison': 0.5, 'ground': 2, 'flying': 0.5, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1,
                            'dragon': 0.5, 'dark': 1, 'steel': 0.5, 'fairy': 1},
                  'ice': {'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 1, 'grass': 2, 'ice': 0.5, 'fighting': 1,
                          'poison': 1, 'ground': 2, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1,
                          'dragon': 2, 'dark': 1, 'steel': 0.5, 'fairy': 1},
                  'fighting': {'normal': 2, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 2, 'fighting': 1,
                               'poison': 0.5, 'ground': 1, 'flying': 0.5, 'psychic': 0.5, 'bug': 1, 'rock': 2, 'ghost': 0,
                               'dragon': 1, 'dark': 2, 'steel': 2, 'fairy': 0.5},
                  'poison': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 1,
                             'poison': 0.5, 'ground': 0.5, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 0.5,
                             'dragon': 1, 'dark': 1, 'steel': 0, 'fairy': 2},
                  'ground': {'normal': 1, 'fire': 2, 'water': 1, 'electric': 2, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                             'poison': 2, 'ground': 1, 'flying': 0, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1,
                             'dragon': 1, 'dark': 1, 'steel': 2, 'fairy': 1},
                  'flying': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 0.5, 'grass': 2, 'ice': 1, 'fighting': 2,
                             'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 1,
                             'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1},
                  'psychic': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2,
                              'poison': 2, 'ground': 1, 'flying': 1, 'psychic': 0.5, 'bug': 1, 'rock': 1, 'ghost': 1,
                              'dragon': 1, 'dark': 0, 'steel': 0.5, 'fairy': 1},
                  'bug': {'normal': 1, 'fire': 0.5, 'water': 1, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 0.5,
                          'poison': 0.5, 'ground': 1, 'flying': 0.5, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 0.5,
                          'dragon': 1, 'dark': 2, 'steel': 0.5, 'fairy': 1},
                  'rock': {'normal': 1, 'fire': 2, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 2, 'fighting': 0.5,
                           'poison': 1, 'ground': 0.5, 'flying': 2, 'psychic': 1, 'bug': 2, 'rock': 1, 'ghost': 1,
                           'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1},
                  'ghost': {'normal': 0, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                            'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 2,
                            'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 1},
                  'dragon': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                             'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                             'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 0},
                  'dark': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                           'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 0.5,
                           'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 0.5},
                  'steel': {'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'grass': 1, 'ice': 2, 'fighting': 1,
                            'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1,
                            'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 2},
                  'fairy': {'normal': 1, 'fire': 0.5, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2,
                            'poison': 0.5 , 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                            'dragon': 2, 'dark': 2, 'steel':0.5 , 'fairy': 1}
                 }

    modifier = type_table[attacker_type][defender_type]

    damage = int(round(max(1, (attacker_atk - defender_def + random.randint(-2,5) * modifier))))

    return damage

def Team_Fight(team_one,team_two):
    # set up teams with health status
    team_one_battling = []
    team_two_battling = []

    # adds each pokemon to its team, with 'healthy' status
    for poke in team_one:
        this_poke = {}
        this_poke['status'] = 'healthy'
        this_poke['poke'] = poke
        this_poke['hp'] = poke.hp
        team_one_battling.append(this_poke)

    for poke in team_two:
        this_poke = {}
        this_poke['status'] = 'healthy'
        this_poke['poke'] = poke
        this_poke['hp'] = poke.hp
        team_two_battling.append(this_poke)

    #return team_one_battling, team_two_battling

    # Now we fight with both teams
    Keep_Fighting = True

    while Keep_Fighting == True:
        if Check_Still_Alive(team_one_battling) and Check_Still_Alive(team_two_battling):
            team_one_living = []
            [team_one_living.append(poke) for poke in team_one_battling if poke['status'] == 'healthy']
            team_one_fighter = random.choice(team_one_living)

            team_two_living = []
            [team_two_living.append(poke) for poke in team_two_battling if poke['status'] == 'healthy']
            team_two_fighter = random.choice(team_two_living)

            winner, winner_hp, loser = One_On_One_Fight(team_one_fighter, team_one_fighter['hp'], team_two_fighter, team_two_fighter['hp'])

            # so...using this info, we need to set the loser's status to 'faint'
            # the mistake is here...

            if team_one_fighter == winner:
                for poke in team_one_battling:
                    if poke == team_one_fighter:
                        if winner_hp > 0:
                            poke['hp'] = winner_hp
                        elif winner_hp < 1:
                            poke['hp'] = 0
                            poke['status'] = 'faint'
                for poke in team_two_battling:
                    if poke == loser:
                       poke['hp'] = 0
                       poke['status'] = 'faint'
            if team_two_fighter == winner:
                    for poke in team_two_battling:
                        if poke == team_two_fighter:
                            if winner_hp > 0:
                                poke['hp'] = winner_hp
                            elif winner_hp < 1:
                                poke['hp'] = 0
                                poke['status'] = 'faint'
                    for poke in team_one_battling:
                        if poke == loser:
                           poke['hp'] = 0
                           poke['status'] = 'faint'
        else:
            Keep_Fighting = False
        print team_one_battling
        for poke in team_one_battling:
            print poke['status'], poke['poke'].name, poke['hp'], 'team one'

    return

def Check_Still_Alive(team):
    Is_Still_Alive = True
    sum = 0
    for poke in team:
        if poke['status'] == 'healthy':
            sum += 1
    if sum == 0:
        Is_Still_Alive = False
    return Is_Still_Alive

# Walking through a 'round'
def One_On_One_Fight(poke_one, poke_one_hp, poke_two, poke_two_hp):
    if poke_one['poke'].speed > poke_two['poke'].speed:
        faster_poke = poke_one
        faster_poke_hp = poke_one_hp
        slow_poke = poke_two
        slow_poke_hp = poke_two_hp
    elif poke_two['poke'].speed > poke_one['poke'].speed:
        faster_poke = poke_two
        faster_poke_hp = poke_two_hp
        slow_poke = poke_one
        slow_poke_hp = poke_one_hp
    else:
        faster_poke = poke_one
        faster_poke_hp = poke_one_hp
        slow_poke = poke_two
        slow_poke_hp = poke_two_hp

    print faster_poke['poke'].name, slow_poke['poke'].name
    print faster_poke_hp, slow_poke_hp

    # all the attacks
    while faster_poke_hp > 0 and slow_poke_hp > 0:

        # faster_poke attacks
        damage_output = Calculate_Dp(faster_poke['poke'].attack, faster_poke['poke'].type, slow_poke['poke'].defense, slow_poke['poke'].type)
        print (faster_poke['poke'].name + ' attacks for ' + str(damage_output) + ' ' + str(faster_poke['poke'].type) +' damage!')
        slow_poke_hp = slow_poke_hp - damage_output
        print (slow_poke['poke'].name + ' has ' + str(slow_poke_hp) + ' hp left!')
        print '|'*slow_poke_hp
        print '...'

        # slow_poke attacks
        damage_output = Calculate_Dp(slow_poke['poke'].attack, slow_poke['poke'].type, faster_poke['poke'].defense, faster_poke['poke'].type)
        print (slow_poke['poke'].name + ' attacks for ' + str(damage_output) + ' ' + str(slow_poke['poke'].type) +' damage!')
        faster_poke_hp = faster_poke_hp - damage_output
        print (faster_poke['poke'].name + ' has ' + str(faster_poke_hp) + ' hp left!')
        print '|'*faster_poke_hp
        print '...'

        raw_input('')

    # passing winner / lose values back to Team_Fight
    # faster_poke = max(poke_one, poke_two, key=lambda p:p.speed)

    if faster_poke_hp < 1:
        round_winner = slow_poke
        round_winner_hp = slow_poke_hp
        round_loser = faster_poke
    else:
        round_winner = faster_poke
        round_winner_hp = faster_poke_hp
        round_loser = slow_poke

    # only the winner is standing...
    print 'the battle is over'
    print 'the winner is ', round_winner['poke'].name, ' with ', round_winner_hp, ' hp left!'
    print round_loser['poke'].name, ' has fainted!'
    return round_winner, round_winner_hp, round_loser
