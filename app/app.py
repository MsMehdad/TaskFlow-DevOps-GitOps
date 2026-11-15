
import os
import time

import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "taskflow"),
        user=os.getenv("DB_USER", "taskflow"),
        password=os.getenv("DB_PASSWORD", "taskflow123")
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if title:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO tasks (title) VALUES (%s)",
                (title,)
            )
            conn.commit()
            cur.close()
            conn.close()

        return redirect("/")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM tasks ORDER BY id DESC")
    tasks = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
