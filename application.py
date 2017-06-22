import datetime
import json
import os
import random
import string

import requests

import httplib2
from database_setup import *
from flask import session as login_session
from flask import (Flask, flash, jsonify, make_response, redirect,
                   render_template, request, url_for)
from oauth2client.client import FlowExchangeError, flow_from_clientsecrets
from sqlalchemy import asc, create_engine, desc, exc
from sqlalchemy.orm import sessionmaker

# flask instance and connect to goolge account
app = Flask(_name_)
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog"
# database
engine = create_enigine('sqlite://catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# login
# anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(string.ascii_uppercase
                      + string.digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# GConnect
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # verfy state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        respons.headers['Content-Type'] = 'application/json'
        return response
    # get authorization code
    request.get_data()
    code = request.data.decode('utf-8')
    try:
        # turn the code to a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # check the access token
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # submit request and get response
    httpobj = httplib2.Http()
    response = httpobj.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)
    # if error in access token, discard
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # check the access token used by right user
    google_id = credentials.id_token['sub']
    if result['user_id'] != googe_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # check the token is valid for this app
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    stored_access_token = login_session.get('access_token')
    stored_google_id = login_session.get('google_id')
    if stored_access_token is not None and google_id == stored_google_id:
        response = make_response(json.dumps(
            'Current user is alread connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # store the token in session
    login_session['access_token'] = access_token
    login_session['google_id'] = google_id

    # fetch user info
    userinfo_url = "https://wwww.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    reply = requests.get(userinfo_url, params=params)
    data = reply.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email'].one())
    return user.id


def getUserInfo(user_id):
    try:
        user = session.query(User).filter_by(id=user_id).one()
        return user
    except exc.SQLAlchemyError:
        return None


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except exc.SQLAlchemyError:
        return None


# disconnect a user
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user is not connected'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    httpobj = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # clean user session
        del login_session['access_token']
        del login_session['google_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = redirect(url_for('showCatalog'))
        flash("You have Successfully logged out.")
        return response
    else:
        reponse = make_response(json.dumps("Failed to revoke token.", 400))
        response.headers['Content-Type'] = 'application/json'
        return response
