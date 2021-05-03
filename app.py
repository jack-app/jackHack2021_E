from flask import Flask, render_template, request, session, redirect, url_for
import cv2
import os
import create_image
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save("./static/image/upload/bg_image" + os.path.splitext(filename)[1])
        return redirect(url_for('main'))
    else:
        return render_template("upload.html")

@app.route('/main', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        time_result = request.form["time_result"]
        return redirect(url_for('result', time_result = time_result))
    else:
        answer_area_x, answer_area_y = create_image.create_image()
        return render_template("main.html", answer_area_x = answer_area_x, answer_area_y = answer_area_y)

@app.route('/result')
def result():
    # upload_path = "static/image/upload/" + os.listdir("static/image/upload")[0]
    # if upload_path:
    #     os.remove(upload_path)
    print(request.args.get("time_result"))
    result = request.args.get("time_result")
    return render_template("result.html", result = result)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)