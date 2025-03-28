

from character import create_character, load_characters, save_character, CSV_FILE
from battle import battle
import csv
import matplotlib.pyplot as plt
import pandas as pd
import easygui as eg

def analyze_characters():
    
    #Analyze character attribute data and create report
 
 
    #Exception Handling:
        # Catches Error for missing data with error messages
        # Uses easygui for user choice
 
    #Mean, med and min/max:
        #Mean: Average attribute value
        # Median: Middle value of attribute distribution
        # Min/Max: Attribute value boundaries
 
        # pandas for data processing
        # easygui for UI operations
    characters = load_characters()
    if not characters:
        # A function of easygui can let users see information in a more interesting form
        eg.msgbox("No character data available for analysis")
        return
    
    df = pd.DataFrame(characters)
    numeric_cols = ['hp', 'attack', 'defense', 'speed', 'level', 'experience']
    
    try:
        stats_data = {
            'Mean': df[numeric_cols].mean(),
            'Median': df[numeric_cols].median(),
            'Min': df[numeric_cols].min(),
            'Max': df[numeric_cols].max()
        }
        
        stats_df = pd.DataFrame(stats_data).T.round(2)
        analysis_result = "=== Character Attribute Analysis ===\n"
        analysis_result += stats_df.to_string()
        
        eg.textbox("Analysis Results", "Data Analysis", analysis_result)
        
    except KeyError as e:
        eg.msgbox(f"Data analysis error: Missing required field {e}", "Error")

def show_characters_virtual():

    #Visualizes character attributes

        #matplotlib.pyplot (imported as plt)
        #easygui (imported as eg for message dialogs)
    characters = load_characters()
    if not characters:
        eg.msgbox("No characters found", "Character Display")
        return
    
    plt.ioff()
    for char in characters:
        fig = plt.figure(num=char['name'])
        attributes = ['HP', 'Attack', 'Defense', 'Speed', 'Level', 'Experience']
        values = [char['hp'], char['attack'], char['defense'],
                 char['speed'], char['level'], char['experience']]
        
        bars = plt.bar(attributes, values)
        plt.title(f"{char['name']}'s Attributes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}',
                    ha='center', va='bottom')
        plt.show(block=False)

def save_all_characters(characters):
    
    #Saves all character data to a CSV file
    
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for c in characters:
            writer.writerow([c['name'], c['hp'], c['attack'], c['defense'], 
                           c['speed'], c['level'], c['experience'], c['story']])

def main_menu():
    menu_text = """=== Battle Simulator ===
    1. Create Character
    2. Show Characters (Visual)
    3. Start Battle
    4. Data Analysis
    5. Exit"""
    
    while True:
        choice = eg.enterbox(menu_text, "Main Menu", default="")
        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
        else:
            eg.msgbox("Invalid input! Please enter number 1-5", "Error")
            return 0

def character_selection(characters):
    
    #Presents users with a numbered list of characters

    #easygui for UI

    char_list = "\n".join([f"{i+1}. {c['name']}" for i, c in enumerate(characters)])
    while True:
        input_str = eg.enterbox(f"Select two characters.\nSeparate numbers with spaces(for example 1 2):\n{char_list}", 
                              "Character Selection", 
                              default="")
        if not input_str:
            return None
        
        try:
            nums = list(map(int, input_str.split()))
            if len(nums) != 2:
                raise ValueError
            if nums[0] == nums[1]:
                eg.msgbox("Cannot select the same character!", "Error")
                continue
            return [n-1 for n in nums]
        except (ValueError, IndexError):
            eg.msgbox("Invalid input! Please enter two different numbers", "Error")

def main():
    while True:
        try:
            choice = main_menu()
            if choice == 1:
                character = create_character()
                save_character(character)
                eg.msgbox(f"Character {character['name']} created!\nStory {character['story']}", "Success")
                
            elif choice == 2:
                show_characters_virtual()
                
            elif choice == 3:
                characters = load_characters()
                if len(characters) < 2:
                    eg.msgbox("Need at least 2 characters to battle", "Error")
                    continue
                
                indices = character_selection(characters)
                if indices:
                    try:
                        c1, c2 = characters[indices[0]], characters[indices[1]]
                        battle(c1, c2)
                        save_all_characters(characters)
                    except IndexError:
                        eg.msgbox("Invalid character selection", "Error")
                        
            elif choice == 4:
                analyze_characters()
                
            elif choice == 5:
                break
            else:
                break;
                
        except TypeError:  # Handle window close
            break

if __name__ == "__main__":
    main()
