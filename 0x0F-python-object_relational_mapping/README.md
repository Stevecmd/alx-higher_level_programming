# 0x0F. Python - Object-relational mapping
## Background Context
In this project, you will link two amazing worlds: Databases and Python!+
In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.
In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM). 

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```sh

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

```
With an ORM:
```sh

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()

```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something. 


### General

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

### More Info
- Install and activate venv

To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```sh
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
- Install MySQLdb module version 2.0.x

```sh
(myenv) stevecmd@DESKTOP-UTB295U:~$ sudo apt-get install python3-dev
(myenv) stevecmd@DESKTOP-UTB295U:~$ sudo apt-get install libmysqlclient-dev
(myenv) stevecmd@DESKTOP-UTB295U:~$ sudo apt-get install zlib1g-dev
(myenv) stevecmd@DESKTOP-UTB295U:~$ pip install mysqlclient

```
Confirm succesfull installation of MySQL in the virtual environment:

``sh
    (myenv) stevecmd@DESKTOP-UTB295U:~$ python3
    Python 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import MySQLdb
    >>> MySQLdb.version_info 
    (2, 2, 4, 'final', 0)
```

- Install SQLAlchemy module version 1.4.x
```sh
(myenv) stevecmd@DESKTOP-UTB295U:~$ pip install SQLAlchemy
...
(myenv) stevecmd@DESKTOP-UTB295U:~$ python3
Python 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'2.0.31'
```

## Requirements
### General


- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version `2.0.x`
- Your files will be executed with `SQLAlchemy` version `1.4.x`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy

## More Info
### Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```sh

$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate

```
### Install MySQLdb module version 2.0.x

For installing MySQLdb, you need to have MySQL installed.
```sh

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)

```

### Install `SQLAlchemy` module version `1.4.x`
```sh
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
Also, you can have this warning message:
```sh
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```
You can ignore it.

#### Starting up MYSQL
```sh

root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# sudo service mysql start
 * Starting MySQL database server mysqld                                                                                                           [ OK ] 
root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# sudo service mysql status
 * /usr/bin/mysqladmin  Ver 8.0.28-0ubuntu0.20.04.3 for Linux on x86_64 ((Ubuntu))
Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version          8.0.28-0ubuntu0.20.04.3
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/run/mysqld/mysqld.sock
Uptime:                 42 sec

Threads: 2  Questions: 8  Slow queries: 0  Opens: 117  Flush tables: 3  Open tables: 36  Queries per second avg: 0.190

```

#### Stopping MySQL
```sh

root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# sudo service mysql stop
 * Stopping MySQL database server mysqld 

root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# sudo service mysql status
 * MySQL is stopped.

```

## Tasks
0. Get all states
Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```sh

root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql | mysql -uroot -p
Enter password: 
root@094bfbccda27:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')

```
File: `0-select_states.py`