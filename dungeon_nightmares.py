import random

level_name = "Dungeon_Nightmares_Lvl 1"
player_name = input("Welcome peasant to the Dungeon Nigtmares! What is your peasant name?")
player_health = 100 
inventory = []
main_hand = ''
off_hand = ''
player_score = 0

possible_enemies = ["goblin", "giant spider", "orc"]

orc_damage = 45
giant_spider_damage = 32 
goblin_damage = 12

possible_encounters = ["enemy","friend"]

def print_stats():
    print("===============Player Stats===============")
    print(f"Name: {player_name}")
    print(f"Health: {player_health}")
    print(f"Level: {level_name}")
    print(f"Experience: {player_score}")

while True:

    action = input("Give me action to move or stop")
    
    # Stop or Move in the game loop 
    if (action == 'stop'):
        break 
    else: 
        encounter = random.choice(possible_encounters)

        # (1) Random, Enemy or Friend? 
        if(encounter == 'enemy'):

            enemy = random.choice(possible_enemies)

            print(f"A {enemy} appeared!!! Fight!")

            if (enemy == 'goblin'):
                enemy_damage =  goblin_damage
                player_score += 5
            elif (enemy == 'giant spider'):
                enemy_damage = giant_spider_damage
                player_score += 20
            else: 
                enemy_damage = orc_damage
                player_score += 40

            player_health = player_health - enemy_damage 

            print(f" {enemy} did {enemy_damage} to you.")

        else:

            print("Nothing hostile here...")
        
        print_stats()




def calc_probs_enemies():

    orc_counter = 0 
    spider_counter = 0
    goblin_counter = 0

    for i in range (0,10):
        
        enemy = random.choice(possible_enemies)

        if (enemy == possible_enemies[0]):
            goblin_counter+=1
        elif (enemy == possible_enemies[1]):
            spider_counter+=1
        else:
            orc_counter +=1


    prob_goblin = round(goblin_counter/(goblin_counter + spider_counter + orc_counter),2)
    prob_orc = round(orc_counter/(goblin_counter + spider_counter + orc_counter),2)
    prob_spider = round(spider_counter/(goblin_counter + spider_counter + orc_counter),2)

    print(f"Goblin prob: {prob_goblin} Orc prob: {prob_orc} Spider prob: {prob_spider}")
