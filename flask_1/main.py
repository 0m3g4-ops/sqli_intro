from flask import *
import sqlite3
app=Flask(__name__)
print("opened!!")
con=sqlite3.connect("scoreboard.db")
con.execute('CREATE TABLE leaders (team TEXT,score INTEGER)')
print("created !!")
cur=con.cursor()
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("perfect blue",15000) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("Gryffindor",14900) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("InfoSecIITR",14500) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("ALLES!",14100) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("Doxepticons",13500) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("SDS LABS",13000) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("MOODY ji",12900) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("Lannister",12000) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("Starks",11900) )
cur.execute("INSERT INTO leaders (team,score) VALUES (?,?)",("Noobies",10000) )
con.commit()
con.close()
print("Added")
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
#payload="a";UPDATE leaders SET score = 9999999 where team = 'InfoSecIITR'
