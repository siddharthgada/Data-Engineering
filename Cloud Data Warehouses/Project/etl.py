#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


# In[ ]:


def load_staging_tables(cur, conn):
    '''This function loads data from AWS S3 into Redshift staging tables using the COPY command.'''
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


# In[ ]:


def insert_tables(cur, conn):
    ''' This function loads data from staging tables into the final analytics tables in the Redshift database.'''
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

# In[ ]:


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()

