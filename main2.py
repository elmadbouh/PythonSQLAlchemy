from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import pandas as pd


engine = create_engine('sqlite:///my-sqlite.db')

meta = MetaData()

person = Table(
   	'person', meta, 
   	Column('id', Integer, primary_key = True), 
   	Column('name', String), 
	Column('age', Integer),
	Column('city', String) 
)


meta.create_all(engine)


def add_person(name, age, city):

	stmt = person.insert().values(name=name, age=age, city=city)
	conn = engine.connect()
	result = conn.execute(stmt)

	print(name +" has been added to the database")

def delete_person(id):

	stmt = person.delete().where(person.c.id == id)
	conn = engine.connect()
	conn.execute(stmt)
	
	print(f"Person with id = {id} has been deleted from the database")
	
def update_person(id, name, age, city):

	stmt = person.update().where(person.c.id == id).values(name=name, age=age, city=city)
	conn = engine.connect()
	conn.execute(stmt)

	print(f"Person with id = {id} has been updated")


def get_all():
	df = pd.read_sql_table('person', engine)
	
	print(df.head())

mode = input("Please select mode 1-3 or press enter to display all\n 1-Add\n 2-Delete\n 3-Change\n : ")

match mode:
	case '1': 

		name = input("Please enter a name: ")
		age = input("Please enter an age: ")
		city = input("Please enter a city: ")

		add_person(name, age, city)

	case '2':

		id = input("Please enter the id of the person you want to delete: ")

		delete_person(id)

	case '3':

		id = input("Please enter the id of the person you want to update: ")
		name = input("Please enter the new value for name: ")
		age = input("Please enter the new value for age: ")
		city = input("Please enter the new value for city: ")

		update_person(id, name, age, city)

	case _:

		get_all()
	