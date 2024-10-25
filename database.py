import sqlite3
from flask import g
import os

DATABASE = 'rule_engine.db'

def get_db():
    db = sqlite3.connect('rules.db')
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with db:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(script_dir, 'schema.sql')
        with open(schema_path, 'r') as f:
            db.executescript(f.read())

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()