# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

def battle(character1, character2):
    """
    Turn-based combat system with real-time visualization and progression mechanics
    
    Simulates a battle between two characters with dynamic stats tracking,
    experience-based progression, and interactive graphical representation.
       
    Dependencies:
        - matplotlib for visualization
        - random for damage variation
    
    Behavior Flow:
        1. Initialize visualization with starting stats
        2. Alternate turns based on speed comparison
        3. Execute attack sequence:
            a. Calculate and apply damage
            b. Update visualization
            c. Check defeat condition
            d. Award experience if applicable
        4. Terminate on victory/draw
        5. Clean up visualization resources
    """
    # turn based battle between two characters.
    print(f"\nBattle Start: {character1['name']} VS {character2['name']}")
    max_rounds = 100    #Set maximum number of turns
    round_count = 0

    def init_visualization(left_char, right_char):
        plt.ion()
        fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 6))
        
        update_visualization(fig, ax_left, ax_right, left_char, right_char, "Battle Start!")
        return fig, ax_left, ax_right
    
    def update_visualization(fig, ax_left, ax_right, left, right, action_text):
        ax_left.clear()
        ax_right.clear()
        fig.suptitle(action_text, fontsize=12, color='darkred', y=0.98)
        ax_left.barh(['HP', 'Attack', 'Defense', 'Speed', 'Level', 'Experience'],
                    [left['hp'], left['attack'], left['defense'], 
                     left['speed'], left['level'], left['experience']])
        ax_left.set_title(f"{left['name']}")
        ax_right.barh(['HP', 'Attack', 'Defense', 'Speed', 'Level', 'Experience'],
                     [right['hp'], right['attack'], right['defense'],
                      right['speed'], right['level'], right['experience']])
        ax_right.set_title(right['name'])
        
        plt.pause(1)
    # attack turn tracker
    def attack_turn(attacker, defender):
        # Simulates an attack turn between two characters.
        # Calculates damage based on attacker's attack and defender's defense.
        damage = random.randint(int(attacker['attack'] * 0.8), attacker['attack']) - defender['defense']
        damage = max(0, damage)  # Ensure damage is not negative
        defender['hp'] -= damage
        print(f"{attacker['name']} attacks {defender['name']} for {damage} damage! Remaining HP: {defender['hp']}")

    # Check if a character is defeated
    def is_defeated(character):
        # Checks if a character's HP is less than or equal to 0.
        return character['hp'] <= 0

    # experience to the winner
    def award_experience(winner, loser):
        # experience to the winner based on the loser's level.
        # If experience reaches 100, the winner levels up.
        experience_gain = loser['level'] * 10
        winner['experience'] += experience_gain
        print(f"{winner['name']} gains {experience_gain} experience points!")
        if winner['experience'] >= 100:
            winner['level'] += 1
            winner['experience'] = 0
            winner['hp'] += 20
            winner['attack'] += 5
            winner['defense'] += 5
            winner['speed'] += 1
            print(f"{winner['name']} leveled up to level {winner['level']}!")

    fig, ax_left, ax_right = init_visualization(character1, character2)
    # Battle loop
    while True:
        if round_count >= max_rounds:
            print("\nBattle ends in a draw due to too many rounds!")
            break
        round_count += 1
        if character1['speed'] >= character2['speed']:
            attack_turn(character1, character2)
            attack_info = f"{character1['name']} attacks {character2['name']}!"
            update_visualization(fig, ax_left, ax_right, character1, character2, attack_info)
            if is_defeated(character2):
                award_experience(character1, character2)
                print(f"{character2['name']} is defeated! {character1['name']} wins!\n")
                break
            attack_turn(character2, character1)
            attack_info = f"{character2['name']} attacks {character1['name']}!"
            update_visualization(fig, ax_left, ax_right, character1, character2, attack_info)
            if is_defeated(character1):
                award_experience(character2, character1)
                print(f"{character1['name']} is defeated! {character2['name']} wins!\n")
                break
        else:
            attack_turn(character2, character1)
            attack_info = f"{character2['name']} attacks {character1['name']}!"
            update_visualization(fig, ax_left, ax_right, character1, character2, attack_info)
            if is_defeated(character1):
                award_experience(character2, character1)
                print(f"{character1['name']} is defeated! {character2['name']} wins!\n")
                break
            attack_turn(character1, character2)
            attack_info = f"{character1['name']} attacks {character2['name']}!"
            update_visualization(fig, ax_left, ax_right, character1, character2, attack_info)
            if is_defeated(character2):
                award_experience(character1, character2)
                print(f"{character2['name']} is defeated! {character1['name']} wins!\n")
                break
    plt.ioff()
    plt.close()