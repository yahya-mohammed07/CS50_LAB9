from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":

    # get data after hitting sumbit
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    # insert into database
    db.execute("INSERT INTO birthdays(name, month, day) VALUES (?,?,?)", name, month, day)

    # go back to / and see new results
    return redirect("/")

  else:
    res = db.execute("SELECT * FROM birthdays")
    return render_template("index.html", res=res)

@app.route('/remove', methods=["GET","POST"])
def remove():

  if request.method == "POST":
    id = request.form.get("id")
    db.execute("DELETE FROM birthdays where id=?", id)
    return redirect("/")

  return redirect("/")
