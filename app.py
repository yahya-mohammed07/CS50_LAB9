from flask import Flask, redirect, render_template, request
import sqlite3 as sql

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# connect to database
connect = sql.connect("birthdays.db", check_same_thread=False)

# get database
db = connect.cursor()


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":

    # get data after hitting sumbit
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    # insert into database
    db.execute("INSERT INTO birthdays(name, month, day) VALUES (?,?,?)", (name, month, day) )
    connect.commit()
    # go back to / and see new results
    return redirect("/")

  else:
    res = db.execute("SELECT * FROM birthdays")
    col = [desc[0] for desc in db.description]
    results = []

    # making a list of dicts
    for row in res:
      summary = dict(zip(col, row))
      results.append(summary)

    return render_template("index.html", res=results)

@app.route('/remove', methods=["GET","POST"])
def remove():

  if request.method == "POST":
    id = request.form.get("id")
    db.execute("DELETE FROM birthdays where id=?", (id) )
    return redirect("/")

  return redirect("/")
