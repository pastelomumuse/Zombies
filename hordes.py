# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for
from entities import *
from local import secret_key
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/home")
@app.route("/bank")
def home():
    return("En construction !")

@app.route("/signup", methods=['GET', 'POST'])
@db_session
def signup():
    if request.method == 'POST':
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        Joueur(login=login, email=email, password=password)
        commit()
        return("Enregistrement effectué")
    else:
        return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
@db_session
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        joueur = Joueur.get(login=login)
        if joueur is not None and joueur.check_password(password): #joueur is none if login doesn't exist
            session['login'] = joueur.login
            return redirect(url_for('index'))
        else:
            return("Mauvaise combinaison pseudo/mot de passe !")
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    sql_debug(True)
    db.generate_mapping(create_tables=True)
    app.secret_key = secret_key
    app.run(host='::', debug=True)
