from flask import Flask, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return make_response({"message":"ok"},200)

app.run("0.0.0.0", 5000)