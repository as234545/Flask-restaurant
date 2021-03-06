from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for,send_file
from flask_login import login_user,logout_user, login_required,LoginManager, current_user
import os
from sqlalchemy.orm import sessionmaker
from database import *
import bcrypt
import json
from werkzeug.security import generate_password_hash, check_password_hash
from keystoneclient.session import Session
import sqlite3
from datetime import datetime, timedelta, time


def get_db_connection():
    conn = sqlite3.connect('db6.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    res = Resturants.query.all()
    return render_template('index.html', res = res)

@app.route('/profile')
@login_required
def profile():
    print(current_user.name)
    res = Resturants.query.all()
    return render_template('profile.html', name=current_user.name , res = res )



@app.route('/signup')
def signup():
    return render_template('sighnup2.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash("Thie user already exists")
        return redirect(url_for('signup'))
    
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    print(password)
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    print(user)
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials

    login_user(user, remember=remember)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login2.html')



@app.route('/reservation', methods=['GET','POST'])
@login_required
def Reservation1():
    es = Resturants.query.all()
    guestNum = int(request.args.get('num'))
    date = request.args.get("date")
    date = date.replace('T', '') 
    date3 = datetime.strptime(date, "%Y-%m-%d%H:%M")
    textarea = request.args.get('textarea')
    res_id = request.args.get('res_id')
    opstion = request.args.get('comp_select')
    if date3 < datetime.now():
        flash("please choose a future date ")
        return redirect(url_for('Reservation2' ,res_id = res_id ))

    new_order = Reservation( guestnum = guestNum , date = date3, menutype = opstion, notes = textarea , user_id = current_user.id)
    print("4444444")
    db.session.add(new_order)
    db.session.commit()



    flash("Reservation Conformed!")
    return redirect(url_for('index'))



@app.route('/reservation/<int:res_id>', methods=['GET'])
@login_required
def Reservation2(res_id):
    res = Resturants.query.filter_by(id=res_id).first()
    #res = Resturants.query.all()
    num = request.form.get('num')
    date = request.form.get('date')
    textarea = request.form.get('textarea')
    print(date)


    return render_template('user_page.html', res = res, res_id = res_id )

@app.route('/reservation/', methods=['GET'])
@login_required
def Reservation3():
    res_id = request.args.get('res_id')
    int(res_id)
    return redirect(url_for('Reservation2' ,res_id = res_id ))



if __name__ == "__main__":
    app.secret_key = 'testing'
    app.run(debug=True,port=4000)
