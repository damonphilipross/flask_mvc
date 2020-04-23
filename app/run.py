from flask import request
from flask import render_template
from flask import Flask
# from app.templates import index
app = Flask(__name__)


def hello_world():
    return 'Hello, World!'

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.form:
    print(request.form)
  return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
