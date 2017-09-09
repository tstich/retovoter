from flask import Flask, render_template, url_for

retovoter = Flask(__name__)

@retovoter.route('/')
def home():
    return render_template('index.html')

@retovoter.route('/vote')
def vote():
    return render_template('vote.html')

if __name__ == '__main__':
    retovoter.run()