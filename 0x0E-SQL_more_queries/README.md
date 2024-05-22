# 0x0E. SQL - More queries
### General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Requirements
### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE…`)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## Comments for your SQL file:
```sh

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

```
## Install MySQL 8.0 on Ubuntu 20.04 LTS
```sh

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

```
Connect to your MySQL server:
```sh

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye

```

### How to import a SQL dump
```sh

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller

```

## Tasks
0. My privileges!

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# service mysql start  
 * Starting MySQL database server mysqld                                                                                                           [ OK ] 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-list_databases.sql | mysql -uroot -p 
cat: 0-list_databases.sql: No such file or directory
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# ls
README.md
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 0-privileges.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 2: There is no such grant defined for user 'user_0d_1' on host 'localhost'
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
ERROR 1141 (42000) at line 5: There is no such grant defined for user 'user_0d_2' on host 'localhost'

```

File: `0-privileges.sql`

1. Root user 
Write a script that creates the MySQL server user `user_0d_1`.

- `user_0d_1` should have all privileges on your MySQL server
- The `user_0d_1` password should be set to `user_0d_1_pwd`
- If the user `user_0d_1` already exists, your script should not fail


```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 1-create_user.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION
ERROR 1141 (42000) at line 5: There is no such grant defined for user 'user_0d_2' on host 'localhost'

```

File: `1-create_user.sql`

2. Read user 

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only SELECT privilege in the database hbtn_0d_2
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 2-create_read_user.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION
Grants for user_0d_2@localhost
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`

```


File: `2-create_read_user.sql`

3. Always a name 

Write a script that creates the table `force_name` on your MySQL server.

- `force_name` description:
    - `id` INT
    - `name` VARCHAR(256) can’t be null
- The database name will be passed as an argument of the `mysql` command
- If the table `force_name` already exists, your script should not fail

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 3-force_name.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id      name
89      Best School
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id      name
89      Best School

```

File: `3-force_name.sql`

4. ID can't be null 

Write a script that creates the table `id_not_null` on your MySQL server.

- `id_not_null` description:
    - `id` INT with the default value 1
    - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `id_not_null` already exists, your script should not fail

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 4-never_empty.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id      name
89      Best School
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id      name
89      Best School
1       Best

```
File: `4-never_empty.sql`

5. Unique ID 

Write a script that creates the table `unique_id` on your MySQL server.

- `unique_id` description:
    - `id` INT with the default value 1 and must be unique
    - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `unique_id` already exists, your script should not fail

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 5-unique_id.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id      name
89      Best School
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id      name
89      Best School

```
File: `5-unique_id.sql`

6. States table 

Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

- `states` description:
    - `id` INT unique, auto generated, can’t be null and is a primary key
    - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `states` already exists, your script should not fail

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 6-states.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name
1       California
2       Arizona
3       Texas

```
File: `6-states.sql`

7. Cities table 
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

- `cities` description:
    - `id` INT unique, auto generated, can’t be null and is a primary key
    - `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
    - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `cities` already exists, your script should not fail

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 7-cities.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      state_id        name
1       1       San Francisco
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      state_id        name
1       1       San Francisco

```
File: `7-cities.sql`

8. Cities of California 
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

- The `states` table contains only one record where `name = California` (but the id can be different, as per the example)
- Results must be sorted in ascending order by `cities.id`
- You are not allowed to use the `JOIN` keyword
- The database name will be passed as an argument of the `mysql` command

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 8-cities_of_california_subquery.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name
1       California
2       Arizona
3       Texas
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      state_id        name
1       1       San Francisco
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name
1       San Francisco

```
File: `8-cities_of_california_subquery.sql`

9. Cities by States 

Write a script that lists all cities contained in the database `hbtn_0d_usa`.

- Each record should display: `cities.id` - `cities.name` - `states.name`
- Results must be sorted in ascending order by `cities.id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

```sh

root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# emacs 9-cities_by_state_join.sql
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name
1       California
2       Arizona
3       Texas
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      state_id        name
1       1       San Francisco
root@356e29ffef03:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name    name
1       San Francisco   California

```
File: `9-cities_by_state_join.sql`

10. Genre ID by show






File: `10-genre_id_by_show.sql`

11. Genre ID for all shows 





File: `11-genre_id_all_shows.sql`

12. No genre





File: `12-no_genre.sql`

13. Number of shows by genre 




File: `13-count_shows_by_genre.sql`

14. My genres 




File: `14-my_genres.sql`

15. Only Comedy




File: `15-comedy_only.sql`

16. List shows and genres 





File: `16-shows_by_genre.sql`