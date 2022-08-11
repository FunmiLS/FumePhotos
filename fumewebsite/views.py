#Store the user navigation pages
#Blueprint allows you to organise files nicely
from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def enter():
    return render_template("enter.html")

@views.route('/home') #URL to get to this end point
def home():
    return render_template("home.html")

@views.route('/collections/') #URL to get to this end point
def collection():
    return render_template("collections.html")


@views.route('/videos') #URL to get to this end point
def videos():
    return render_template("videos.html")

@views.route('/prints') #URL to get to this end point
def prints():
    return render_template("prints.html")
