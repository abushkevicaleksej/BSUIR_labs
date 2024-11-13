from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from controller import Controller



if __name__ == "__main__":
    ct = Controller()
    ct.run()


