from flask import Flask

#Creating app to run website server
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AMAZE balls'

#Importing the blueprints
    from .views import views
    from .auth import auth #Delete later
    from .collections import collections

    app.register_blueprint(auth, url_prefix='/')  # delete later
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(collections, url_prefix='/collections/')

    return app
