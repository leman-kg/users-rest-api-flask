import os
from dotenv import load_dotenv
from flask import Flask, render_template

# local modules
from services.database import db
from services.routes import default, users

load_dotenv()

# initiate app and db connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('DB_TRACK_MODS')
db.init_app(app)

# HACK: create non-existing db tables using existing models
with app.app_context():
    db.create_all()

# Just a home page
@app.route("/")
def home():
    return render_template('index.html')

# registering routes
app.register_blueprint(default)
app.register_blueprint(users)

if __name__ == '__main__':
    app.run()
