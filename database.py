import sqlite3
import uuid


conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_db():
    c.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            password TEXT,
            age INTEGER,
            xp INTEGER,
            role TEXT  
        )
    """)



def insert_all():
    many_user = [
        (str(uuid.uuid4()), 'John', 'Hann', '123_cat@gmail.com', '123', 17, 0, 'novice'),
        (str(uuid.uuid4()), 'Karl', 'Misy', 'KarlM@gmail.com', 'sss', 29, 10, 'explorer'),
        (str(uuid.uuid4()), 'Cumb', 'Amy', 'Ammmy@gmail.com', 'shoes', 45, 50, 'master')
    ]
    c.executemany("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)", many_user)


def insert_customer():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    age = int(input("Age: "))
    xp = 0
    role = 'novice'


    user_id = str(uuid.uuid4())

    
    c.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (user_id, first_name, last_name, email, password, age, xp, role))

    print(f"Utilizatorul {first_name} {last_name} a fost adăugat cu ID-ul {user_id}.")


def printf():
    c.execute("SELECT * FROM user")
    items = c.fetchall()
    print("Users:")
    print("________________________________")
    for item in items:
        print(item)

def rank(user):
    if user.xp > 15:
        user.role = 'explorer'
    if user.xp > 65:
        user.role = 'pioner'



def passw():
    print("Password not strong enough for:")
    print("________________________________")
    print("Set stronger password:")
    print(" ")
    c.execute("UPDATE user SET password = 'iuski379os' WHERE password LIKE '123%' OR password LIKE '%789'")


def backup_all():
    with sqlite3.connect('data.db') as conn:
        with open('user_bkp.db', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)


def restore_all():
    conn.close()  
    with open('user_bkp.db', 'r') as f:
        sql = f.read()
    with sqlite3.connect('data.db') as conn:
        conn.executescript(sql)



create_db()  
insert_all()  
printf()  
passw()  
insert_customer()  
printf() 
backup_all()  

conn.commit()  
conn.close() 
