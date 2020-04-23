from flask import request
from flask import render_template
from flask import Flask
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from models.models import Model

import os



project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(
    os.path.join(project_dir, "database.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.form:
    new_item = Model(name=request.form.get('name'))
    db.session.add(new_item)
    print(request.form)
  return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
