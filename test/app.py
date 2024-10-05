import json
import os
from flask import Flask, jsonify, request, send_file, send_from_directory, render_template

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__, template_folder="templates")

# os.environ["GOOGLE_API_KEY"]="AIzaSyCze4GCQSD8NXYPweVjv7uC9poghVckLLA"
@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/settings')
def index():
    return render_template('settings.html')

if __name__=="__main__":
    app.run(debug=True)


