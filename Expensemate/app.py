from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "expenses.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"income": 0, "fixed": [], "general": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


@app.route("/")
def home():
    data = load_data()
    return render_template("index.html", data=data)


@app.route("/add", methods=["POST"])
def add():
    data = load_data()
    category = request.form.get("category")
    amount = float(request.form.get("amount"))
    name = request.form.get("name", "")

    if category == "income":
        data["income"] = amount
    elif category == "fixed":
        data["fixed"].append({"name": name, "amount": amount})
    elif category == "general":
        data["general"].append({"name": name, "amount": amount})

    save_data(data)
    return render_template("index.html", data=data)


@app.route("/reset", methods=["POST"])
def reset():
    save_data({"income": 0, "fixed": [], "general": []})
    return render_template("index.html", data={"income": 0, "fixed": [], "general": []})


if __name__ == "__main__":
    app.run(debug=True)
