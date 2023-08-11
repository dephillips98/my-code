import sqlite3
conn = sqlite3.connect("mini.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS cohort
        (id INTERGER PRIMARY KEY, name TEXT)''')


def insert_data(cohort_id, name):
    c.execute("SELECT * FROM cohort WHERE id=?", (cohort_id,))
    existing_row = c.fetchone()

    if existing_row:
        # A row with the same id already exists, you can choose to update or skip
        print(f"Row with id {cohort_id} already exists.")
    else:
        c.execute("INSERT INTO cohort (id, name) VALUES (?, ?)", (cohort_id, name))
        print(f"Inserted data with id {cohort_id}")

c.execute("INSERT INTO cohort (id, name) VALUES (1, 'alex')")
c.execute("INSERT INTO cohort (id, name) VALUES (2, 'benji')")
c.execute("INSERT INTO cohort (id, name) VALUES (3, 'nor')")
c.execute("INSERT INTO cohort (id, name) VALUES (4, 'erik')")
c.execute("INSERT INTO cohort (id, name) VALUES (5, 'sam')")
c.execute("INSERT INTO cohort (id, name) VALUES (6, 'sal')")
c.execute("INSERT INTO cohort (id, name) VALUES (7, 'mari')")
c.execute("INSERT INTO cohort (id, name) VALUES (8, 'cay')")\

donn = sqlite3.connect("mini_qual.db")
d = donn.cursor()
d.execute('''CREATE TABLE IF NOT EXISTS qualities
        (id INTERGER PRIMARY KEY, quality TEXT, FOREIGN KEY(name_id) REFERENCES cohort(id))''')

d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (1, 'tally', 2)")
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (2, 'gamery', 7)")
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (3, 'drivery', 3)")
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (4, 'warlocky', 6)")
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (5, 'sporty', 4)",)
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (6, 'codey', 1)")
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (7, 'south sidery', 8)")
d.execute("INSERT INTO qualities (ids, quality, name_id) VALUES (8, 'funny', 5)")






conn.close()
conn.commit()
donn.commit()
donn.close()


'''
aonn = sqlite3.connect("mini.db")
a = aonn.cursor()
'''
#a.execute('''CREATE TABLE IF NOT EXISTS cohort
#        (id INTERGER PRIMARY KEY, name TEXT)''')
'''
a.execute("INSERT INTO cohort (id, name) VALUES (1, 'alex')")
a.execute("INSERT INTO cohort (id, name) VALUES (2, 'benji')")
a.execute("INSERT INTO cohort (id, name) VALUES (3, 'nor')")
a.execute("INSERT INTO cohort (id, name) VALUES (4, 'erik')")
a.execute("INSERT INTO cohort (id, name) VALUES (5, 'sam')")
a.execute("INSERT INTO cohort (id, name) VALUES (6, 'sal')")
a.execute("INSERT INTO cohort (id, name) VALUES (7, 'mari')")
a.execute("INSERT INTO cohort (id, name) VALUES (8, 'cay')")
'''
