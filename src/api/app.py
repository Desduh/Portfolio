from flask import app, Flask, render_template, url_for
import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/menu')
def menu():
    return render_template('menu_inicial.html')

@app.route('/passatempo')
def passatempo():
    return render_template('passatempo.html')

@app.route('/profissional')
def profissional():
    return render_template('profissional.html')

@app.route('/sobre_mim')
def sobre():
    date = datetime.date.today()
    year = int(date.strftime("%Y"))
    month = int(date.strftime("%m"))
    day = int(date.strftime("%d"))

    if month == 6:
            if day >= 7:
                old = year - 2004
    else:
        if month >= 6:
            old = year - 2004
        else:
            old = year - 2005
        
    return render_template('sobre_mim.html', old=old)

if __name__ == '__main__':
    app.run(debug=True)