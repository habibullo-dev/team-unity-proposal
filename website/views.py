from flask import Flask, Blueprint, render_template, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')