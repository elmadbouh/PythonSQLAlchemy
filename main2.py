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

	ins = person.insert().values(name = name, age=age, city=city)
	conn = engine.connect()
	result = conn.execute(ins)

	print(name +" has been added to the database")

def get_all():
	df = pd.read_sql_table('person', engine)
	
	print(df.head())

mode = input("Please select mode 1-4:\n 1-Select\n 2-Add\n 3-Change\n 4-Delete\n  : ")

match mode:
	case 1:
		get_all()

	case 2: 

		name = input("Please enter a name: ")
		age = input("Please enter an age: ")
		city = input("Please enter a city: ")

		add_person(name, age, city)

	
