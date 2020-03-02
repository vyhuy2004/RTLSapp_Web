from flask import Flask, render_template, g, request, session, redirect, url_for
from database import get_db

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secretkeyforme'

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'postgres_db_cur'):
        g.postgres_db_cur.close()

    if hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn.close()

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


if __name__ == '__main__':
    app.run()
