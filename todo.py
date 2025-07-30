from urllib.parse import quote_plus
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
username = quote_plus(os.getenv("Amaravathi_2002"))
password = quote_plus(os.getenv("Amara_2002"))
# MongoDB setup
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.karnc11.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["todo_db"]
todos = db["todos"]

# Display all tasks
@app.route("/")
def index():
    all_todos = list(todos.find())
    return render_template("index.html", todos=all_todos)
