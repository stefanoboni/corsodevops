from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def hello_devops():
    return jsonify(hello="DevOps")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)