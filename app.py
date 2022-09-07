import os
from flask import Flask, render_template
app = Flask(__name__)
#sets the background color of web page
color = "green"
#setting up environment variable APP_COLOR
#color_bkg = os.environ.get("APP_COLOR")

@app.route("/")
def main():
  #print(color)
  return render_template('index.html', color=color)

@app.route("/hello")
def hello():
  #print(color)
  return render_template('hello.html')

if __name__ == "__main__":
  app.run()

