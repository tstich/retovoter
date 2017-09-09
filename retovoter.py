from flask import Flask, flash, render_template, url_for, request, redirect

retovoter = Flask(__name__)

@retovoter.route('/')
def home():
    return render_template('index.html')

@retovoter.route('/vote', methods=['GET','POST'])
def vote():
    if request.method == 'POST':
        value = request.form['vote']
        print('Value: ' + value)

        return redirect(url_for('home'))

    return render_template('vote.html')

if __name__ == '__main__':
    retovoter.run()