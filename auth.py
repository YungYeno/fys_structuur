from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask
from models import User
from __init__ import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # return html template
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    flightnumber = request.form.get('flightnumber')
    seatnumber = request.form.get('seatnumber')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not user.seatnumber == seatnumber or not user.flightnumber == flightnumber:
        flash('Please check your details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exists or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


# # ALS ER EEN SIGNUP FUNCTIE NODIG IS!
# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')
#
#
# @auth.route('/signup', methods=['POST'])
# def signup_post():
#     # Code to validate and add user to database goes here
#     flightnumber = request.form.get('flightnumber')
#     email = request.form.get('email')
#     seatnumber = request.form.get('seatnumber')
#
#     # If this query returns a user then the e-mail already exists in the database
#     user = User.query.filter_by(email=email).first()
#
#     # if a user is found, we want to redirect back to signup page so user can try again
#     if user:
#         flash('Email address already exists')
#         return redirect(url_for('auth.signup'))
#     # create a new user with the form data.
#     new_user = User(flightnumber=flightnumber, email=email, seatnumber=seatnumber)
#
#     # add new user to the database
#     db.session.add(new_user)
#     db.session.commit()
#
#     return render_template('auth.login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))