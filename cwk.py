

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import login_user, current_user, logout_user, login_required
import cgi
from markupsafe import escape
import os
import jinja2
from werkzeug.security import check_password_hash, generate_password_hash
from db import db, User


app = Flask(__name__)

#route to the index

      #return render_template('index.html', README=readme.read(), requirements=req.read())

@app.route("/register", methods=["GET","POST"])
def register():
  if(request.method == "POST"):
    Fname = request.form["Fname"]
    Lname = request.form["Lname"]
    Email = request.form["Email"]
    password = request.form["password"]
    code = request.form["Code"] or ""
    if(code == ""):
      user = User(Fname,Lname,Email,generate_password_hash(password),False)
      db.session.add(user)
      return redirect("/login")

    elif(code == "Dc5_G1gz"):
      user = User(Fname,Lname,Email,generate_password_hash(password),True)
      db.session.add(user)
      return redirect("/login")

    else:
      return redirect("/register")

  else:
    return render_template("/register")

      
@app.route("/login", methods=["GET","POST"])
def login():
  if(request.method == "POST"):
    email = request.form["Email"]
    password = request.form["password"]
    user = User.query.filter_by(Email = email).first()
    #checks if the user exists
    if(user != "" or user != None):
      passwordHash = user.password
      #checks is the password match
      if(check_password_hash(passwordHash,password)):
        session["Email"] = email
        login_user(user)
      else:
        print("Wrong password")
        return redirect("/login")
    else:
      print("please enter a username")
      return redirect("/login")
  #request is GET
  else:
    return render_template("/login")

@app.route('/')
def index():
  events = Event.query
    return render_template('index.html')

      




    






