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

lessons = [
    ("Фортепиано","https://www.youtube.com/playlist?list=PLIiklUOW1Aj64LRlEdfFlpaSaq2RPZWO3","ГБУДО г. Москвы ДМШ им. К.Н.Игумнова",88,"Иванов И.А","http://igumnov.music.mos.ru/"),
    ("Струнные инструменты","https://yandex.ru/video/preview/13657299184609103752","ГБУДО г. Москвы ДМШ им. К.Н.Игумнова",85,"Иванова Е.А","http://igumnov.music.mos.ru/"),
    ("духовые и ударные инструменты","https://www.youtube.com/watch?v=54xgZH3FulA","ГБУДО г. Москвы ДМШ им. К.Н.Игумнова",88,"Петров П.П.","http://igumnov.music.mos.ru/"),
    ("народные инструменты","https://ok.ru/video/372259620109","ГБУДО г. Москвы ДМШ им. К.Н.Игумнова",88,"Сидоров К.А","http://igumnov.music.mos.ru/"),
]

lessons_records = ", ".join(["%s"] * len(lessons))

levels = [
    ("LITE","Кто сочиняет музыку?","Композитор","Текст","Композитор – автор, создатель музыкальных произведений","Композитор – автор, создатель музыкальных произведений"),
    ("INTERMEDIATE","Как называется инструмент, в котором одна из клавиатур напоминает клавиатуру фортепиано?","Аккордеон","Текст","Аккордеон – музыкальный инструмент, в котором  правая клавиатура фортепианного типа, то есть, напоминает клавиатуру фортепиано.","Аккордеон – музыкальный инструмент, в котором  правая клавиатура фортепианного типа, то есть, напоминает клавиатуру фортепиано./"),
    ('HARD',"Как называется музыкальный спектакль, содержание которого воплощается через музыку и танец?","Балет","Текст","Балет – вид сценического искусства, содержание которого выражается в музыкально-хореографических образах","Балет – вид сценического искусства, содержание которого выражается в музыкально-хореографических образах"),
]

levels_records = ", ".join(["%s"] * len(levels))

maps = [
    ("ГБУДО г. Москвы ДМШ им. К.Н.Игумнова","ул. Покровка, 39, стр. 3, Москва","+7 (495) 917-56-77","dmshigumnova@culture.mos.ru","ГБУДО г. Москвы «Детская музыкальная школа имени К.Н. Игумнова»","Школа – одна из старейших в городе Москве. Она была основана в 1920 году и носит имя известного русского пианиста, профессора Московской консерватории К.Н. Игумнова. Основательницей и первым директором школы была Е.С. Вартазарянц, ученица К.Н. Игумнова, выпускница Московской консерватории. Непосредственное участие К.Н. Игумнова в становлении и работе школы стало тем прочным фундаментом, который определил развитие школы, её профессиональные традиции.",
     "Академическое пение, Духовые и ударные инструменты, Народные инструменты, Струнные инструменты,Фортепиано,Теория музыки,Хоровое пение,Платное отделение"),
]

maps_records = ", ".join(["%s"] * len(maps))

ribbons = [
    ("События в ГБУДО г. Москвы ДМШ им. К.Н.Игумнова","Какие концерты будут в июне 2023 г?","Концерт О. Газманова","Характер талантливых детей","Интерью с О. Газмановым",
"25.05.23","25.05.23","Академическое пение, Духовые и ударные инструменты, Народные инструменты, Струнные инструменты,Фортепиано,Теория музыки,Хоровое пение,Платное отделение","https://yandex.ru/profile/182606330694"),
]

ribbons_records = ", ".join(["%s"] * len(ribbons))

sds = [
    ("Фортепиано",88,"Фортепиано",13,"Фортепиано",2,"ГБУДО г. Москвы ДМШ им. К.Н.Игумнова","Фортепиано",48,"духовые и ударные инструменты",2,"Фортепиано",37,0),
    ("струнные инструменты",45,"струнные инструменты",4,"",0,"ГБУДО г. Москвы ДМШ им. К.Н.Игумнова","струнные инструменты",18,"народные инструменты",2,"струнные инструменты",8,0),
    ("духовые и ударные инструменты",40,"духовые и ударные инструменты",6,"",0,"ГБУДО г. Москвы ДМШ им. К.Н.Игумнова","духовые и ударные инструменты",22,"хоровое пение",6,"духовые и ударные инструменты",22,0),
    ("народные инструменты",34,"народные инструменты",6,"",0,"ГБУДО г. Москвы ДМШ им. К.Н.Игумнова","народные инструменты",39,"сольное академическое пение",1,"народные инструменты",7,0),
]

sds_records = ", ".join(["%s"] * len(sds))


sps = [
    ("Кто сочиняет музыку?","Композитор","Композитор – автор, создатель музыкальных произведений"),
    ("Как называется инструмент, в котором одна из клавиатур напоминает клавиатуру фортепиано?","Аккордеон","Аккордеон – музыкальный инструмент, в котором  правая клавиатура фортепианного типа, то есть, напоминает клавиатуру фортепиано."),
    ("Как называется музыкальный спектакль, содержание которого воплощается через музыку и танец?","Балет","Балет – вид сценического искусства, содержание которого выражается в музыкально-хореографических образах"),
]

sps_records = ", ".join(["%s"] * len(sps))

uws = [
    ("Katerina-810@mail.r","https://www.behance.net/KateBunakova","Бунакова Екатерина","https://www.behance.net/KateBunakova",0,"",99),
    ("ariamsaab1983@gmail.com","https://vk.com/alenakozachenko","Козаченко Алена","https://vk.com/alenakozachenko",0,"",99),
    ("labworkspace@yandex.ru",'',"Лабунский Андрей","",0,"",99),
    ("nikulin9810@yandex.ru","","Никулин Алексей","",0,"",99),
    ("pochta201002@mail.ru","https://vk.com/id1240707","Степанов Андрей","https://vk.com/id1240707",0,'',99),
]

uws_records = ", ".join(["%s"] * len(uws))


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

insert_query = (
    f"INSERT INTO lessons (lesson,lessonref,uchr,rating,teacher,uchrmap) VALUES {lessons_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, lessons)

insert_query = (
    f"INSERT INTO levels (levels,tasktext,answer,tasktype,explanation1,explanation2) VALUES {levels_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, levels)

insert_query = (
    f"INSERT INTO maps (uchr,address,phone,mail,description,features,pernapr) VALUES {maps_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, maps)

insert_query = (
    f"INSERT INTO ribbon (news,questions,dayword,talentedchildren,interview,birthday,dates,napr,mapref) VALUES {ribbons_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, ribbons)

insert_query = (
    f"INSERT INTO studydirections (pernapr1,kol1,pernapr2,kol2,pernapr3,kol3,uchr,pernapr4,kol4,pernapr5,kol5,pernapr6,kol6,year) VALUES {sds_records}"
)
connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, sds)


insert_query = (
    f"INSERT INTO studyplan (task,answer,contentinfo) VALUES {sps_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, sps)

insert_query = (
    f"INSERT INTO userway (email,userref,username,userphoto,age,reffortest,rating) VALUES {uws_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, uws)


select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

select_comps = "SELECT * FROM competitions"
comps = execute_read_query(connection, select_comps)

for comp in comps:
    print(comp)

select_lessons = "SELECT * FROM lessons"
lessons = execute_read_query(connection, select_lessons)

for lesson in lessons:
    print(lesson)

select_levels = "SELECT * FROM levels"
levels = execute_read_query(connection, select_levels)

for level in levels:
    print(level)


select_maps = "SELECT * FROM maps"
maps = execute_read_query(connection, select_maps)

for map in maps:
    print(map)

select_ribbons = "SELECT * FROM ribbon"
ribbons = execute_read_query(connection, select_ribbons)

for ribbon in ribbons:
    print(ribbon)

select_sds = "SELECT * FROM studydirections"
sds = execute_read_query(connection, select_sds)

for sd in sds:
    print(sd)

select_sps = "SELECT * FROM studyplan"
sds = execute_read_query(connection, select_sps)

for sp in sps:
    print(sp)

select_uws = "SELECT * FROM userway"
sds = execute_read_query(connection, select_uws)

for uw in uws:
    print(uw)










