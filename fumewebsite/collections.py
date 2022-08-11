from flask import Blueprint, render_template


collections = Blueprint('collections', __name__)

@collections.route('being-biracial')
def biracial():
    return render_template("biracial.html")

@collections.route('away-with-the-pixie')
def fairy():
    return render_template("away.html")

@collections.route('what-shade-is-nude')
def nude():
    return render_template("nude.html")

@collections.route('film')
def film():
    return render_template("film.html")

