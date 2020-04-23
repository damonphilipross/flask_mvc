from app.run import db

class ModelPrototype(db.Model):
  name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)

  def __repr__(self):
    return '<Name: {}>'.format(self.title)
