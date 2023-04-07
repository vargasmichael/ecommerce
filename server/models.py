from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

db = SQLAlchemy(metadata=metadata)

class Manager(db.Model, SerializerMixin):
    __tablename__ = 'managers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    player = db.relationship('Player', backref='managers')
    serialize_rules = ('-players.managers',)
    
    @validates('name')
    def check_length(self, key, value):
        if len(value) >= 2:
            return value
        else:
            raise Exception('Not valid length.')

class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String, nullable=False)
    sport = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer, nullable=True)

    player = db.relationship('Player', backref='teams')
    serialize_rules = ('-players.teams',)
    
    @validates('sport')
    def check_sport(self, key, value):
        if value in ['football', 'basketball', 'baseball', 'hockey', 'soccer']:
            return value
        else:
            raise Exception('Not valid sport.')
    
    @validates('name', 'city')
    def check_length(self, key, value):
        if len(value) >= 2:
            return value
        else:
            raise Exception('Not valid length.')
       
       
    @validates('founding_year')
    def check_founding_year(self, key, value):
        if 1900 <= value <= 2023:
            return value
        else:
            raise Exception('Too old.')
    
class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    manager_id = db.Column(db.Integer, db.ForeignKey('managers.id'))
    
    serialize_rules = ('-teams.players', '-managers.players')
    
    @validates('salary')
    def check_salary(self, key, value):
        if value >= 0:
            return value
        else: 
            raise Exception('Go make that bread.')
        
    @validates('name')
    def check_length(self, key, value):
        if len(value) >= 2:
            return value
        else:
            raise Exception('Not valid length.')
            
        
