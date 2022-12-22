from flask import Flask, jsonify, request, render_template
from flask import Blueprint, render_template


app = Flask(__name__, template_folder='templates')
Server = Blueprint('Server', __name__)

@Server.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("stats.txt", boolean = True)
    
    
