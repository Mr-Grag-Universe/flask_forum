from flask import Flask, render_template

def home_render():
    return render_template("home.html")