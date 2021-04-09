import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://ygleqmpxarndti:5cb1c211804ea25f0db6fe1ef81dd5d27189b5dac5316c692d557695693cde22@ec2-54-205-183-19.compute-1.amazonaws.com:5432/d8r7v2amje5jed
'
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project One: TODO"

if  __name__ =='__main__':
    app.run(debug=True)
