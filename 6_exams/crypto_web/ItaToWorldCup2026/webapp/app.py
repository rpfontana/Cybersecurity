import os
import sqlite3 as sql
import threading
import time
from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "spritz{Azzurri_hacked_back_to_the_World_Cup}"

# Shared state between the HTTP handlers and the background monitor.
state = {
    "flag_revealed": False,
    "groups_generated": False,
}


def _connect():
    return sql.connect("database.db")


def db_monitor():
    """Background thread.

    Watches the `teams` table while the bracket is still open.
    If Italy is added BEFORE the groups have been generated, the monitor
    accepts the (illegitimate) qualification, builds the groups including
    the Azzurri and unlocks the flag on the login page.
    Once the groups are generated the teams table is considered frozen.
    """
    while True:
        try:
            con = _connect()
            cur = con.cursor()
            cur.execute("SELECT generated FROM status WHERE id=1")
            row = cur.fetchone()
            generated = row[0] if row else 0

            if not generated:
                cur.execute("SELECT name FROM teams")
                names = [r[0].lower() for r in cur.fetchall()]
                italy_in = any(("ital" in n) for n in names)

                if italy_in:
                    cur.execute("SELECT name FROM teams ORDER BY id")
                    teams = [r[0] for r in cur.fetchall()]
                    cur.execute("DELETE FROM groups_table")
                    for i, t in enumerate(teams):
                        g = chr(ord('A') + (i % 12))
                        cur.execute(
                            "INSERT INTO groups_table (group_name, team_name) VALUES (?, ?)",
                            (g, t),
                        )
                    cur.execute("UPDATE status SET generated=1 WHERE id=1")
                    con.commit()
                    state["flag_revealed"] = True
                    state["groups_generated"] = True
            else:
                state["groups_generated"] = True
            con.close()
        except Exception:
            pass
        time.sleep(2)


def retrieveUser(username, password):
    con = _connect()
    cur = con.cursor()
    # Hand-built SQL: the developer kept the original "simple and readable"
    # f-string query and only switched from execute() to executescript() so
    # that the same handler could also run maintenance batches.
    query = (
        f"SELECT id, username FROM `users` "
        f"WHERE username='{username}' AND password='{password}'"
    )
    try:
        cur.executescript(query)
    except Exception:
        pass
    con.commit()
    con.close()

    # Authentication itself is performed against a separate prepared statement
    # so that normal users can still log in even though executescript()
    # cannot return rows.
    con = _connect()
    cur = con.cursor()
    cur.execute(
        "SELECT id, username FROM users WHERE username=? AND password=?",
        (username, password),
    )
    user = cur.fetchone()
    con.close()
    return {'id': user[0], 'username': user[1]} if user is not None else None


@app.route('/', methods=['POST', 'GET'])
def home():
    flag = FLAG if state["flag_revealed"] else None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = retrieveUser(username, password)
        except Exception:
            user = None
        # Re-check the flag: the injection may have just triggered the monitor.
        if state["flag_revealed"]:
            flag = FLAG
        if user is None:
            return render_template('index.html', nologin=[1], flag=flag)
        return render_template('bracket.html', user=user, flag=flag)
    return render_template('index.html', flag=flag)


# Start the background monitor as soon as the module is imported, so it
# runs both under `flask run` and under `python app.py`.
monitor_thread = threading.Thread(target=db_monitor, daemon=True)
monitor_thread.start()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
