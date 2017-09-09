from flask import Flask, flash, render_template, url_for, request, redirect, session
from flask.ext import shelve
import uuid

retovoter = Flask(__name__)

retovoter.secret_key = '\x9d\xa2\x03\x1d\xef\xa5JK"\x8czi_Y\xe6\xb2\xfa\x0c\xba\xa8xL\xaf\xd9'
retovoter.config['SHELVE_FILENAME'] = 'votes.db'
shelve.init_app(retovoter)

@retovoter.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Create new Season
        season_uuid = str(uuid.uuid4())
        with shelve.get_shelve('c') as db:
            db[season_uuid] = {
            'users': set(),
            'votes': [{}]
            }

        session['role'] = 'moderator'
        return url_for('vote', _external=True)+'?season='+season_uuid

    return render_template('index.html')

def user_id():
    if 'user' not in session:
        session['user'] = str(uuid.uuid4())
    return session['user']

def season_id():
    if 'season' not in session or request.args.get('season'):
        session['season'] = request.args.get('season')

    return session['season']

@retovoter.route('/vote', methods=['GET','POST'])
def vote():
    season_key = season_id()
    user = user_id()

    if request.method == 'POST':
        value = request.form['vote']

        with shelve.get_shelve('c') as db:
            season = db[season_key]
            season['users'].add(user)
            season['votes'][0][user] = value
            db[season_key] = season
            print(season)

        return redirect(url_for('home'))

    return render_template('vote.html')

if __name__ == '__main__':
    retovoter.run()