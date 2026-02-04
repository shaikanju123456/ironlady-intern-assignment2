from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "").lower()

    if "student" in query:
        reply = "Iron Lady offers leadership and career readiness programs for students."
    elif "fresher" in query:
        reply = "Iron Lady supports freshers with career clarity and professional skills."
    elif "working" in query or "professional" in query:
        reply = "Iron Lady provides leadership growth programs for working professionals."
    else:
        reply = "Please enter student, fresher, or working professional."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
