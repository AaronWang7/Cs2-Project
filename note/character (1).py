# -*- coding: utf-8 -*-
import csv
import random
import os
from faker import Faker
from faker.providers import BaseProvider

class FantasyStoryProvider(BaseProvider):
    def fantasy_background(self):
        elements = [
            f"Born in {fake.city()}",
            f"Raised by {random.choice(['wizards', 'dragons', 'elves', 'dwarves'])}",
            f"Carries a {fake.color_name()} {random.choice(['sword', 'staff', 'shield', 'amulet'])}",
            f"Scar from battle with {random.choice(['demon', 'giant', 'ancient beast'])}",
            f"Seeks the {random.choice(['Holy Grail', 'Dragon Stone', 'Lost Crown'])}",
            f"Whispered prophecy: '{fake.sentence()}'"
        ]
        return " ".join(random.sample(elements, k=3)) + f" {fake.paragraph()}"

CSV_FOLDER = "upgrading_battle_simulator/data"
CSV_FILE = os.path.join(CSV_FOLDER, "characters.csv")
fake = Faker()
fake.add_provider(FantasyStoryProvider)
if not os.path.exists(CSV_FOLDER):
    os.makedirs(CSV_FOLDER)

def create_character(namestr=""):
    name = namestr
    if namestr == "":
        name = fake.name()
    hp = 50
    attack = random.randint(10, 20)
    defense = random.randint(5, 25)
    speed = random.randint(1, 10)
    level = 1
    experience = 0
    story = fake.fantasy_background()
    return {
        'name': name,
        'hp': hp,
        'attack': attack, 
        'defense': defense,
        'speed': speed,
        'level': level, 
        'experience': experience,
        'story': story 
    }

def save_character(character):
    # Saves a character's data to a CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            character['name'],
            character['hp'],
            character['attack'],
            character['defense'],
            character['speed'],
            character['level'],
            character['experience'],
            character['story']
        ])
def load_characters():
    # Loads characters from a CSV file
    # Returns a list of character dictionaries.
    characters = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    characters.append({
                        'name': row[0],
                        'hp': 50,
                        'attack': int(row[2]),
                        'defense': int(row[3]),
                        'speed': int(row[4]),
                        'level': int(row[5]),
                        'experience': int(row[6]),
                        'story': row[7] if len(row) > 7 else ''
                    })
    except FileNotFoundError:
        pass
    return characters
