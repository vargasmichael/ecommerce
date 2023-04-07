from app import app 
from models import db, Team, Player, Manager 
from faker import Faker
from random import randint
import random


faker = Faker()

sport = ['football', 'basketball', 'baseball', 'hockey', 'soccer']

with app.app_context():
    print("Deleting Players")
    Player.query.delete()
    print("Deleting Teams")
    Team.query.delete()
    print("Deleting Managers")
    Manager.query.delete()
    print("Seeding Teams")
    teams = []
    for i in range(15):
        new_team = Team(
            name=faker.name(),
            city=faker.city(),
            sport = random.choice(sport),
            founding_year = randint(1900, 2023)
            )
        teams.append(new_team)
    db.session.add_all(teams)

    print("Seeding Player")
    players = []
    for i in range(200):
        new_player = Player(
            name=faker.name(),
            salary = randint(0, 1000000000),
            team_id = randint(1, 15),
            manager_id = randint(1, 75)
            )
        players.append(new_player)
    db.session.add_all(players)
    
    print("Seeding Managers")
    managers = []
    for i in range(50):
        new_manager = Manager(
            name = faker.name(),
            
            )
        managers.append(new_manager)
    db.session.add_all(managers)
    db.session.commit()