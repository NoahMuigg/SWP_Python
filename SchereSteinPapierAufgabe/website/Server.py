from flask import Flask, jsonify, request, render_template
from flask import Blueprint, render_template
import plotly.graph_objects as go
import json

app = Flask(__name__, template_folder='templates')
Server = Blueprint('Server', __name__)

@Server.route('/', methods=['GET', 'POST'])
def home():
    with open("website/data/stats.txt", "r") as file:
        data = json.load(file)
    return render_template('stats.html', data=data, boolean = True)

@Server.route('/plot', methods=['GET', 'POST'])
def plot():
    with open("website/data/stats.txt", "r") as file:
        data = json.load(file)
    fig = go.Figure(data=[go.Bar(x=list(data.keys()), y=list(data.values()))])
    plot_json = fig.to_json()
    return render_template('home.html', plot_json=plot_json)
   
