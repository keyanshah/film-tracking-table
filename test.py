from flask import Flask, url_for
from flask import render_template
from datetime import datetime

class Row(object):
    def __init__(self,week,film,filmdate,location):
        self.week = week
        self.film = film
        self.filmdate = filmdate
        self.location = location
        self.warnings = ""

        self.findWarnings()

    def findWarnings(self):
        today = datetime.now()

        if self.filmdate == today: 
            if self.location != "Ingested":
                self.warnings = "Film not ingested for showing time!"


app = Flask(__name__)

@app.route('/')
def hello():
    tbl = [Row("1", "Django Unchained", datetime.now(), "Meh")]*6
    url_for("static", filename="style.css")
    return render_template('index.html', table=tbl)

if __name__ == "__main__":
    app.debug = True
    app.run()
    
