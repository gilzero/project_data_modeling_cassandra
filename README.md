# project_data_modeling_cassandra

note: remove aws password before public

# Project Description

Project Github address:
https://github.com/gilzero/project_data_modeling_cassandra

Data modeling with Apache Cassandra and build an ETL pipeline using Python. 
Working with raw event log files and combine the logs. By checking a pre-given queries, create table and validate with read. 
ETL pipeline that transfers data from files into Apache Cassendra. Local solution and AWS solution.


### Local Solution


---

## File Description

- etl.ipynb (general all-in-one notebook)
- create\_tables.py (drop tables if exists and re-create new empty schema tables)
- etl.py (the core ETL script, load, transform and insert data to db)
- sql\_queries.py (a helper script holding raw sql for other functional scripts)
- test.ipynb (for testing data reading from postgres)
- /data/... (raw data source directory, json files inside)
- /crud\_scripts (connection, crud, stored procedures, stored functions etc snippet)


---

## Libraries
- psycopg2
- ipython-sql
- pandas
- numpy
- PrettyTable
- Jupyter Notebook

---

## How to Run:

under project directory, create and activate virtual env (depends on systems), e.g
$ source vene/bin/activate

Install libraries mentioned above.

Then, 
1. run create\_tables.py
$ python create_tables.py 

2. run etl.py
$ python etl.py





---


## Environment

Developed and tested on local MacOS machine. 

Install postgress with homebew.
https://formulae.brew.sh/formula/postgresql

Service Start command:

$brew services start postgresql

pdadmin 4 for postgres MacOS GUI client.

created used pydb. newuser/password
ref:

https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/?utm\_source=pocket\_mylist


bash: 

$psql postgres


CREATE ROLE student WITH LOGIN PASSWORD 'student';
ALTER ROLE student CREATEDB;



## Resolve connection

When encounter session or connection is being occupied, e.g

psycopg2.errors.ObjectInUse: database "sparkifydb" is being accessed by other users
DETAIL:  There is 1 other session using the database.

Issue a restart of postgres
$ brew services restart postgresql


make sure disconnect pgadmin connection,
via pgadmin, right click a db to disconnect





