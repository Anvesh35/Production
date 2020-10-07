import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Get the code to work',0)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Keep up the pace witht he class',1)")
conn.execute("INSERT INTO todo (task,status) VALUES ('workout everyday',1)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Maintain healthy diet',0)")
conn.commit()