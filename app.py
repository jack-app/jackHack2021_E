from flask import Flask, render_template, request, session
import cv2
import create_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/main', methods=['GET'])
def main():
    answer_area_x, answer_area_y = create_image.create_image()
    return render_template("main.html", answer_area_x = answer_area_x, answer_area_y = answer_area_y)

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)