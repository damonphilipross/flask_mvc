from app.run import db

class Model(db.Model):
  name = db.Column(db.string(400), unique=False, nullable=False, primary_key=True)

  def __repr__(self):
    return '<Name: {}>'.format(self.title)
