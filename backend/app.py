from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="../frontend")

feedbacks = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    name = data.get("name")
    message = data.get("message")

    if not name or not message:
        return jsonify({"error": "Both name and message are required"}), 400

    feedbacks.append({"name": name, "message": message})
    return jsonify({"success": True, "message": "Thank you for your feedback!"})

@app.route("/api/feedbacks", methods=["GET"])
def get_feedbacks():
    return jsonify(feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
