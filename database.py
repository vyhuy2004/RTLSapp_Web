from flask import g
import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

def connect_db():
    conn = psycopg2.connect('postgres://uiekgpcgjggxlq:cbe57f0707b34d48d50ac1c49433ffa87c29b37080a31534a19f32170bf0b673@ec2-52-203-160-194.compute-1.amazonaws.com:5432/daub0hhg3j6sa8', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()
    return conn, sql

def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur

def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql','r').read())
    db[1].close() #close cursor

    db[0].close() #close connection
