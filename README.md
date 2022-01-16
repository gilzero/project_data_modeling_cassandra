# project_data_modeling_cassandra

note: remove aws password before public

# Project Description

Project Github address:
https://github.com/gilzero/project_data_modeling_cassandra

Data modeling with Apache Cassandra and build an ETL pipeline using Python. 
Working with raw event log files and combine the logs. By checking a pre-given queries, create table and validate with read. 
ETL pipeline that transfers data from files into Apache Cassendra. 
For this project, I provide local solution (remote workspace) and AWS deployment solution.

About: Apache Cassandra
Apache Cassandra is an open source NoSQL distributed database trusted by thousands of companies for scalability and high 
availability without compromising performance. 
Linear scalability and proven fault-tolerance on commodity hardware or cloud infrastructure make it the perfect platform 
 for mission-critical data. (Some adopters like Apple, Uber, Netflix.)




## Local Solution
file: Project\_1B\_Project\_local.ipynb
This notebook is the solution for Apache Cassandra cluster set up on local machine / workspace.


---

## AWS Solution (Amazon Keyspaces for Apache Cassandra)

file: Project\_1B\_Project\_with\_AWS.ipynb

I have also created a solution that working on actual AWS Keyspaces cluster under Hongkong Region.

Before start, create a user with Keyspaces permission, under IAM settings.

Cluster exists already in region, just connect it.

For this case I use HK region, the cluster address is:
- cassandra.ap-east-1.amazonaws.com

Note that AWS requires to set consistency level for inserting data.
https://docs.datastax.com/en/developer/python-driver/3.25/getting_started/

No need to shutdown cluster as it is persisted in the region.

Make sure remove keyspace once no longer in use, otherwise extra charges may occurred!




---

## How to Run:

Run the ETL via Jupyter notebook.


---


## Environment

Developed and tested on remote workspace and AWS Keyspaces service. 

