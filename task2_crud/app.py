from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        stage = request.form["stage"]
        interest = request.form["interest"]

        conn.execute(
            "INSERT INTO students (name, email, stage, interest) VALUES (?, ?, ?, ?)",
            (name, email, stage, interest)
        )
        conn.commit()

    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    return render_template("index.html", students=students)
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        stage = request.form["stage"]
        interest = request.form["interest"]

        conn.execute(
            "UPDATE students SET name=?, email=?, stage=?, interest=? WHERE id=?",
            (name, email, stage, interest, id)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    conn.close()
    return render_template("edit.html", student=student)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            stage TEXT,
            interest TEXT
        )
    """)
    conn.close()

    app.run(debug=True)
