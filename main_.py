import sqlalchemy as db
import pandas as pd
from model import Person, Base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///my-sqlite.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_person(name, age, city):
	person = Person(name=name, age=age, city=city)
	session.add(person)
	session.commit()

	print(name + " has been added to the database")


def get_all():
	df = pd.read_sql_table('person', engine)
	
	print(df.head())

mode = input("To add a person typ 'add' otherwise press any key: ")

if mode == "add": 

	name = input("Please enter a name: ")
	age = input("Please enter an age: ")
	city = input("Please enter a city: ")

	add_person(name, age, city)

else:
	get_all()
