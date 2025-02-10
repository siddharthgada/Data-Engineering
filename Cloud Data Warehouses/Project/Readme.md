# Project: Data Warehouse for Sparkify

## Introduction:
A music streaming startup, Sparkify, has grown its user base and song database and wants to move its processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, I was tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to.

## Project Steps
1. Create Table Schemas
- Designed schemas for fact and dimension tables using SQL.
- Defined CREATE TABLE statements in sql_queries.py.
- Implemented create_tables.py to connect to Redshift and create the tables.
- Included DROP TABLE IF EXISTS statements to reset the database before creating tables.
- Created a Redshift cluster and an IAM role with S3 read access.
- Configured dwh.cfg with Redshift database and IAM role details.
- Verified table schemas using AWS Redshift Query Editor.
2. Build ETL Pipeline
- Implemented etl.py to:
-- Load raw data from S3 to Redshift staging tables.
-- Transform and insert data into fact and dimension tables.
- Tested the pipeline by running etl.py and validating data in Redshift.
3. Cleanup
- Deleted the Redshift cluster after completing the project to avoid unnecessary costs.

## Schema Design
### Fact Table
- songplays: Stores records of song play events (user activity).
### Dimension Tables
- users: Stores user information.
- songs: Stores song details.
- artists: Stores artist details.
- time: Stores timestamps of song plays.

## Key Learning Outcomes
✅ AWS Redshift: Setting up and managing a cloud-based data warehouse. <br>
✅ SQL & Schema Design: Implementing a star schema with optimized queries.<br>
✅ ETL Process: Loading large datasets efficiently from S3 to Redshift.<br>
✅ Python & Boto3: Automating infrastructure using Python scripts.<br>

## How to Run the Project<br>
1️⃣ Update dwh.cfg with Redshift database and IAM role details.<br>
2️⃣ Run sql_queries.py to create statements to be imported in create_table.py and etl.py files.<br>
3️⃣ Run create_tables.py to create tables in Redshift.<br>
4️⃣ Run etl.py to load and transform data.<br>
5️⃣ Verify data by querying tables in Redshift Query Editor.<br>
6️⃣ Delete Redshift Cluster to avoid charges.<br>

## Technologies Used
🔹 AWS Redshift<br>
🔹 AWS S3<br>
🔹 PostgreSQL (Redshift dialect)<br>
🔹 Python (psycopg2)<br>
