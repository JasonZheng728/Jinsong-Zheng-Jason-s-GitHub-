from flask import Flask, request, render_template,send_from_directory,send_file
import os
import shutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("FileOperation.html")

# 2.0 Upload binary file
@app.route("/upload", methods=["POST", "PUT", "GET"])
def upload():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    my_file = request.files.get("my_file")
    new_file = os.path.join("directory",my_file.filename)
    my_file.save(new_file)

# 2.1 Create binary file
@app.route("/create", methods=["POST", "PUT", "GET"])
def create():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    content = request.args.get("content")
    with open("D:\\temp\\BinaryFile1.js".format(directory, file_name), "wb") as file:
        file.write("This file is implemented in BinaryFile1.js")
'''
# 3.2 Delete binary file
@app.route("/delete", methods=["DELETE", "GET"])
def delete():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    os.remove("D:\\temp\\BinaryFile1.js".format(directory, file_name))
'''
# 3.3 Move binary file
@app.route("/move", methods=["POST", "PUT", "GET"])
def move():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    shutil.move(('D:\\temp\\BinaryFile1.js', 'D:\\temp\\root_dir7\\').format(directory, file_name))

# 3.4 Readfile (returns file content)
# @app.route("/get_file")
# def get_file():
#   return send_file("D:\\temp\\ironman.jpg")
    
@app.route("/read", methods=["GET"])
def read():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    with open("D:\\temp\\BinaryFile1.js".format(directory, file_name), "rb+") as file:
        content = file.readlines()
        return content

if __name__ == "__main__":
    app.run(debug=True)
