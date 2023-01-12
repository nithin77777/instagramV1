import flask
import os

# save this as app.py
from flask import Flask
from flask import Flask, render_template
os.chdir('/Users/nithinsaikrishna/PycharmProjects/pythonProject/instagram/')


app = Flask(__name__)

@app.route("/")






def home():
   return render_template('insta.html')
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5001)