import os
import random

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import clone

clone()
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run():
    tmp_id = str(random.randint(0,999999)).zfill(6)
    while os.path.exists(f"./alterlang-source/workspace/{tmp_id}"):
        tmp_id = str(random.randint(0,999999)).zfill(6)
    data = request.form.get("code")
    print(data)
    with open(f"./alterlang-source/workspace/{tmp_id}.altr","w") as f:
        f.write(data)
    import subprocess


    process = subprocess.Popen(f"python ./alterlang-source/workspace/run.py ./alterlang-source/workspace/{tmp_id}.altr", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out)
    return redirect("/")
