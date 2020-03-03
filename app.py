from flask import Flask, render_template, g, request, session, redirect, url_for
from flask_socketio import SocketIO
from database import get_db

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secretkeyforme'
socketio = SocketIO(app)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'postgres_db_cur'):
        g.postgres_db_cur.close()

    if hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn.close()

@app.route('/')
def index():
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
    return render_template('viewresult.html', result = results)

@app.route('/websocket')
def websocket():
    return render_template('websocket.html')

@socketio.on('message')
def receive_message(message):
    print('########: {}'.format(message))

@socketio.on('sending_event')
def receive_sending_event(message):
    print('ID: {}, X = {}, Y = {}, Z = {}'.format(message['id'],message['x'],message['y'],message['z']))
    socketio.emit('render_page', message)

if __name__ == '__main__':
    socketio.run(app)
