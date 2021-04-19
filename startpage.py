from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route("/")
def startpage():
    return render_template("base.html")
    
@app.route("/", methods=["POST"])
def post_method():
	location = request.form["loc"]
	
	if location != "":
		return redirect(url_for('read_json'))
	else:
		return render_template("base.html")
		
@app.route("/results")
def read_json():
	input_data = open("message.json")
	data = json.load(input_data)
	
	#import pdb; pdb.set_trace()
	
	for k in data:
		print(k["name"], flush=True)
		
	print("cat", flush=True)
	
	#input_data = ["cat", "dog", "squirrel"]
	
	return render_template("results.html", json_data = data)
