
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/GraphPage") #annotations tell which function goes with which request.
def render_page1():
    return render_template('GraphPage.html')

@app.route("/DataFinder")
def render_page2():
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False)
