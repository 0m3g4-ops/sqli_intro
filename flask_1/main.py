from flask import *
import sqlite3
app=Flask(__name__)
"""print("opened!!")
con=sqlite3.connect("scoreboard.db")
con.execute('CREATE TABLE leaders (team TEXT,score INTEGER)')
print("created !!")
cur=con.cursor()
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("I1",150) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("I2",200) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("I3",100) )
con.commit()
con.close()
print("Added")"""
@app.route("/")
def index():
    return render_template("template.html")
@app.route("/leaderboard",methods=["POST"])
def leaderboard():
    payload=request.form["payload"]
    con=sqlite3.connect("scoreboard.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.executescript("select * from leaders where team ="+payload)
    rows=cur.fetchall()
    if rows == []:
        cur.execute("select * from leaders order by score DESC;")
        rows=cur.fetchall()
    return render_template("leaderboard.html",rows=rows)
    
if __name__ == '__main__':
    app.run(debug=True)
#payload="I1";UPDATE leaders SET score = 999999 where team = 'I1'