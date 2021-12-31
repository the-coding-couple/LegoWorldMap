from flask import Flask
from flask.templating import render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database initialization
# app.config['SQLALCHEMY_DATABASE URI'] = 'sqlite:///test.db' # can use mysql or postgresql
# db = SQLAlchemy(app)

@app.route("/")
def index():
    # return "Hello World!"
    return render_template("index.html")

# class Square(db.Model):
#     color_id = 1
#     colored = False
#     colorable = False
# TODO: 19:19

if __name__ == "__main__":
    app.run(debug=True)


# template inheritance