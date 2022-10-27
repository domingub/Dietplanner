from flask import Flask, request, render_template


app= Flask(__name__)




@ app.route('/')
def  homepage():
    return render_template("home_anon.html")  

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404