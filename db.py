import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e} ' occurred")


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_competitions_table = """
CREATE TABLE IF NOT EXISTS Competitions (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL, 
  userprofile TEXT NOT NULL,
  userphone TEXT NOT NULL,
  achievements TEXT NOT NULL,
  rating INTEGER
)
"""

create_lessons_table = """
CREATE TABLE IF NOT EXISTS Lessons (
  id SERIAL PRIMARY KEY,
  lesson TEXT NOT NULL, 
  lessonref TEXT NOT NULL,
  uchr TEXT NOT NULL,
  rating INTEGER,
  teacher TEXT NOT NULL,
  uchrmap TEXT NOT NULL
)
"""

create_levels_table = """
CREATE TABLE IF NOT EXISTS Levels (
  id SERIAL PRIMARY KEY,
  levels TEXT NOT NULL, 
  tasktext TEXT NOT NULL,
  answer TEXT NOT NULL,
  tasktype TEXT NOT NULL,
  explanation1 TEXT NOT NULL,
  explanation2 TEXT NOT NULL
)
"""

create_maps_table = """
CREATE TABLE IF NOT EXISTS Maps (
  id SERIAL PRIMARY KEY,
  uchr TEXT NOT NULL, 
  address TEXT NOT NULL,
  phone TEXT NOT NULL,
  mail TEXT NOT NULL,
  description TEXT NOT NULL,
  features TEXT NOT NULL,
  pernapr TEXT NOT NULL
)
"""

create_ribbon_table = """
CREATE TABLE IF NOT EXISTS Ribbon (
  id SERIAL PRIMARY KEY,
  news TEXT NOT NULL, 
  questions TEXT NOT NULL,
  dayword TEXT NOT NULL,
  talentedchildren TEXT NOT NULL,
  interview TEXT NOT NULL,
  birthday TEXT NOT NULL,
  dates TEXT NOT NULL,
  napr TEXT NOT NULL,
  mapref TEXT NOT NULL
)
"""

create_studydirections_table = """
CREATE TABLE IF NOT EXISTS StudyDirections (
  id SERIAL PRIMARY KEY,
  pernapr1 TEXT NOT NULL, 
  kol1 INTEGER,
  pernapr2 TEXT NOT NULL, 
  kol2 INTEGER,
  pernapr3 TEXT NOT NULL, 
  kol3 INTEGER,
  uchr TEXT NOT NULL,
  pernapr4 TEXT NOT NULL, 
  kol4 INTEGER,
  pernapr5 TEXT NOT NULL, 
  kol5 INTEGER,
  pernapr6 TEXT NOT NULL, 
  kol6 INTEGER,
  year INTEGER
)
"""

create_studyplan_table = """
CREATE TABLE IF NOT EXISTS Studyplan (
  id SERIAL PRIMARY KEY,
  task TEXT NOT NULL, 
  answer TEXT NOT NULL,
  contentinfo TEXT NOT NULL
)
"""

create_userway_table = """
CREATE TABLE IF NOT EXISTS UserWay (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL, 
  userref TEXT NOT NULL,
  username TEXT NOT NULL, 
  userphoto TEXT NOT NULL,
  age INTEGER,
  reffortest TEXT NOT NULL,
  rating INTEGER
)
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS Users (
  id SERIAL PRIMARY KEY,
  login TEXT NOT NULL, 
  pass TEXT NOT NULL,
  role TEXT NOT NULL
)
"""

users = [
    ("BunakovaE", "pass", "Designer"),
    ("ANikulin", "pass1", "Developer"),
    ("AKozachenko", "pass2", "Designer"),
    ("ALabunskiy", "pass3", "Developer"),
    ("AStepanov", "pass4", "Developer"),
]

user_records = ", ".join(["%s"] * len(users))

comps = [
    ("Бунакова","Специалист","+79058235245","Дизайн",99),
    ("Козаченко","Эксперт","","Дизайн",99),
    ("Лабунский","Начинающий","+79254738803","Программист",99),
    ("Никулин","Профессионал","+79269474200","Программист",99),
    ("Степанов","Любитель","+79649903926","Программист",99),
]

comps_records = ", ".join(["%s"] * len(comps))

connection = create_connection(
    "postgres", "postgres", "Pgs2020!comp", "127.0.0.1", "5432")

create_database_query = "CREATE DATABASE estettest"
create_database(connection, create_database_query)
execute_query(connection, create_competitions_table)
execute_query(connection, create_lessons_table)
execute_query(connection, create_levels_table)
execute_query(connection, create_maps_table)
execute_query(connection, create_ribbon_table)
execute_query(connection, create_studydirections_table)
execute_query(connection, create_studyplan_table)
execute_query(connection, create_userway_table)
execute_query(connection, create_users_table)

insert_query = (
    f"INSERT INTO users (login, pass, role) VALUES {user_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, users)

insert_query = (
    f"INSERT INTO competitions (username,userprofile, userphone,achievements, rating) VALUES {comps_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, comps)

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

select_comps = "SELECT * FROM competitions"
comps = execute_read_query(connection, select_comps)

for comp in comps:
    print(comp)








