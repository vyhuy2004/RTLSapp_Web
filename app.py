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
#    db = get_db()

#    loc_cur = db.execute('''select * from location''')
#    loc_result = loc_cur.fetchall()

    return render_template('index.html')
@app.route('/query')
def query():
    id = request.args.get('id')
    x = request.args.get('x')
    y = request.args.get('y')
    z = request.args.get('z')
    db = get_db()
    db.execute('insert into location(id, x, y, z) values (%s, %s, %s, %s);', (id, x, y, z,))
    return '<h1>{} {} {} {}</h1>'.format(id, x, y, z)

@app.route('/viewresult')
def viewresult():
    db = get_db()
    db.execute('select id, x, y, z from location')
    results = db.fetchall()
    return '<h1>ID: {}. X: {}. Y: {}. Z: {}</h1>'.format(results[1]['id'], results[1]['x'], results[1]['y'], results[1]['z'])

if __name__ == '__main__':
    app.run()
