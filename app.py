from flask import Flask, render_template, jsonify
import random
import yaml
import time

app = Flask(__name__)

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

@app.route('/')
def index():
    return render_template("index.html", config=config)

@app.route('/roll', methods=['GET'])
def roll():
    result = random.randint(1, 6)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
