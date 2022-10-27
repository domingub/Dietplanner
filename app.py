from flask import Flask, request, render_template


app= Flask(__name__)


@ app.route('/')
def  login():
    return "content"  

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404