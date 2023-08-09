#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def stat_html():
    #render_template("static_html")
    email = [{"name":"tom", "mail": "tom@.com"},
            {"name": "pom", "mail": "pom@.com"},
            {"name":"rom", "mail": "rom@.com"}
            ]
    return render_template("static_html.html", people=email)
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224, debug = True)
