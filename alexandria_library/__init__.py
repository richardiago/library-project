from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from alexandria_library.config import Config

db = SQLAlchemy(session_options={"autoflush": False})
migrate = Migrate()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from alexandria_library.main.routes import main

    app.register_blueprint(main)
    
    return app