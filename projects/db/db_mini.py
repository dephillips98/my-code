import sqlite3

# Create and populate cohort table
conn = sqlite3.connect("mini.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS cohort
             (id INTEGER PRIMARY KEY, name TEXT)''')

def insert_data(cohort_id, name):
    c.execute("SELECT * FROM cohort WHERE id=?", (cohort_id,))
    existing_row = c.fetchone()

    if existing_row:
        print(f"Row with id {cohort_id} already exists.")
    else:
        c.execute("INSERT INTO cohort (id, name) VALUES (?, ?)", (cohort_id, name))
        print(f"Inserted data with id {cohort_id}")

# Insert data into cohort table
insert_data(1, 'alex')
insert_data(2, 'benji')
insert_data(3, 'nor')
insert_data(4, 'erik')
insert_data(5, 'sam')
insert_data(6, 'sal')
insert_data(7, 'mari')
insert_data(8, 'cay')


# ... insert other data ...

conn.commit()
conn.close()

# Create and populate qualities table
donn = sqlite3.connect("mini_qual.db")
d = donn.cursor()
d.execute('''CREATE TABLE IF NOT EXISTS qualities
             (id INTEGER PRIMARY KEY, quality TEXT, name_id INTEGER, FOREIGN KEY(name_id) REFERENCES cohort(id))''')

def insert_data(qualities_id, name):
     c.execute("SELECT * FROM qualities WHERE id=?", (qualites_id,))
     existing_row = c.fetchone()

     if existing_row:
         print(f"Row with id {cohort_id} already exists.")
     else:
         c.execute("INSERT INTO cohort (id, name) VALUES (?, ?)", (cohort_id, name))
         print(f"Inserted data with id {cohort_id}")
# Insert data into qualities table
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (1, 'tally', 2)")
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (2, 'gamery', 7)")
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (3, 'drivery', 3)")
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (4, 'warlocky', 6)")
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (5, 'sporty', 4)",)
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (6, 'codey', 1)")
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (7, 'south sidery', 8)")
d.execute("INSERT INTO qualities (id, quality, name_id) VALUES (8, 'funny', 5)")


# ... insert other data ...

donn.commit()
donn.close()

