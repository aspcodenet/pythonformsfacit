from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

from lab1Forms import Lab1Form
from lab2Forms import Lab2Form
from lab4Forms import Lab4Form
from lab3Forms import Lab3Form

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route("/lab2", methods=['GET', 'POST'])
def lab2():
    form = Lab2Form()
    if form.validate_on_submit():
        #spara i databas
        return redirect("/RegisterConfirmation?FirstName=Another" )
    return render_template("lab2.html", form=form )



@app.route("/lab3", methods=['GET', 'POST'])
def lab3():
    form = Lab3Form()
    if form.validate_on_submit():
        #spara i databas
        return redirect("/RegisterConfirmation?FirstName=Another" )
    return render_template("lab3.html", form=form )




@app.route("/lab4", methods=['GET', 'POST'])
def lab4():
    form = Lab4Form()
    if form.validate_on_submit():
        
        #spara i databas
        return redirect("/RegisterConfirmation?FirstName=" + form.name.data )
    return render_template("lab4.html", form=form )




@app.route("/lab1", methods=['GET', 'POST'])
def lab1():
    form = Lab1Form()
    if form.validate_on_submit():
        #spara i databas
        return redirect("/RegisterConfirmation?FirstName=" + form.fname.data )
    return render_template("lab1.html", form=form )


@app.route("/RegisterConfirmation")
def RegisterConfirmation():
    FirstName = request.args.get('FirstName', '')
    return render_template("RegisterConfirmation.html", FirstName=FirstName )


if __name__  == "__main__":
    with app.app_context():
        app.run()
        # while True:
        #     print("1. Create")
        #     print("2. List")        
        #     print("3. Exit")                
        #     action = input("Ange:")
        #     if action == "3":
        #         break
        #     if action == "1":
        #         print("Create")
        #     if action == "2":
        #         print("List")          
