from flask import Flask, request, render_template,send_from_directory,send_file
import os
import shutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("FileOperation.html")

# 3.0 Upload log text file
@app.route("/upload", methods=["POST", "PUT", "GET"])
def upload():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    my_file = request.files.get("my_file")
    new_file = os.path.join("directory",my_file.filename)
    my_file.save(new_file)

# 3.1 Create log text file
@app.route("/create", methods=["PUT", "GET", "POST"])
def create():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    content = request.args.get("content")
    with open("D:\\temp\\LogTextFile1.txt".format(directory, file_name), "w+") as file:
        file.write("God Bless Ukraine!")
'''
# 3.2 Delete log text file
@app.route("/delete", methods=["DELETE", "GET"])
def delete():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    os.remove("D:\\temp\\LogTextFile1.txt".format(directory, file_name))
'''
# 3.3 Move log text file
def move():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    shutil.move(('D:\\temp\\LogTextFile1.txt', 'D:\\temp\\root_dir7\\').format(directory, file_name))

# 3.4 Readfile (returns file content)
# @app.route("/get_file")
# def get_file():
#   return send_file("D:\\temp\\LogTextFile1.txt")

# 3.4 Readfile (returns file content)
@app.route("/read", methods=["GET"])
def read():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    with open("D:\\temp\\LogTextFile1.txt".format(directory, file_name), "w+") as file:
        content = file.read()
        return content

# 3.5 Append a line to the end of the log text file
@app.route("/update", methods=["PUT", "GET", "POST"])
def update():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    content = request.args.get("content")
    with open("D:\\temp\\LogTextFile1.txt".format(directory , file_name), "a+") as file:
            content = file.write("Life is short, study Python!")
            return content

if __name__ == "__main__":
    app.run(debug=True)
