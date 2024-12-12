import sqlite3

from flask import Flask, jsonify, make_response, render_template, request

app = Flask(__name__)


# Database setup
def init_db():
    conn = sqlite3.connect("votes.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS votes (id INTEGER PRIMARY KEY, candidate TEXT)"""
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vote", methods=["POST"])
def vote():
    if request.cookies.get("voted") == "true":
        return (
            jsonify({"status": "already_voted"}),
            403,
        )  # 403 Forbidden if already voted

    candidate = request.form.get("candidate")
    if candidate:
        conn = sqlite3.connect("votes.db")
        c = conn.cursor()
        c.execute("INSERT INTO votes (candidate) VALUES (?)", (candidate,))
        conn.commit()
        conn.close()

    # Set a cookie to indicate the user has voted
    response = make_response(jsonify({"status": "success"}))
    response.set_cookie(
        "voted", "true", max_age=60 * 60 * 24
    )  # Cookie expires in 1 day
    return response


@app.route("/results")
def results():
    conn = sqlite3.connect("votes.db")
    c = conn.cursor()
    c.execute("SELECT candidate, COUNT(candidate) FROM votes GROUP BY candidate")
    vote_counts = c.fetchall()
    conn.close()
    return render_template("results.html", vote_counts=vote_counts)


@app.route("/api/results")
def api_results():
    conn = sqlite3.connect("votes.db")
    c = conn.cursor()
    c.execute("SELECT candidate, COUNT(candidate) FROM votes GROUP BY candidate")
    vote_counts = c.fetchall()
    conn.close()
    return jsonify(vote_counts)


@app.route("/reset", methods=["POST"])
def reset_votes():
    conn = sqlite3.connect("votes.db")
    c = conn.cursor()
    c.execute("DELETE FROM votes")
    conn.commit()
    conn.close()
    response = make_response(jsonify({"status": "reset"}))
    response.set_cookie(
        "voted", "", expires=0
    )  # Clear the 'voted' cookie for all users
    return response


if __name__ == "__main__":
    init_db()
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5050, debug=True)
