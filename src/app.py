from flask import Flask, render_template

app = Flask('__name__') 


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
    return render_template('sobre_mim.html')