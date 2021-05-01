from flask import Flask, render_template, request, session
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message="Hello world!")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)