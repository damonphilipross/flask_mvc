from flask import request
from flask import render_template
from flask import Flask
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from models.models import ModelPrototype

import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(
    os.path.join(project_dir, "database.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.form:
    new_item = ModelPrototype(name=request.form.get('name'))
    db.session.add(new_item)
  db_things = ModelPrototype.query.all()
  return render_template("home.html", db_things=db_things)


if __name__ == "__main__":
    app.run(debug=True)
