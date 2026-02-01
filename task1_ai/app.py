from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["query"]
    query = user_input.lower()

    if "student" in query:
        response = "Iron Lady offers leadership and career readiness programs designed for students to build confidence, communication skills, and career clarity."

    elif "fresher" in query:
         response = "For freshers, Iron Lady focuses on helping individuals transition from academics to the professional world through leadership training and mentoring."

    elif "professional" in query:
         response = "Working professionals can benefit from Iron Lady’s leadership programs that focus on growth, decision-making, and career advancement."

    else:    
        response = "Please enter student, fresher, or working professional to know more about relevant programs."

            

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
