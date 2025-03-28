from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from ecomm.retrieval import generate
from ecomm.ingest import ingest_data

app = Flask(__name__)

load_dotenv()

v_store=ingest_data("Data Already Uploaded to AstraDB")
chain=generate(v_store)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)