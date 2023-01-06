from flask import Flask,request,render_template,send_from_directory,send_file
from queue import Queue
import os
import pickle
import shutil

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        if item not in self.queue:
            self.queue.append(item)
            return True
        return False

    def pop(self):
        return self.queue.pop()

    def empty(self):
        if not self.queue:
            return True
        return False

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("FileOperation.html")

#4.1 Create buffer file
@app.route("/create",methods=["POST","PUT","GET"])
def create():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    content = request.args.get("content")
    queue = Queue()
    queue.push(["Apple1","Boy2","Cat3"])
    with open("D:\\temp\\BufferFile1".format(directory , file_name), "wb+") as file:
        pickle.dump(queue, file)
    return "file has been created successfully."

# 4.2 Pop element from buffer file (LIFO)
# @app.route("/get_file")
# def get_file()
    # return send_file("D:\\temp\\BufferFile1")

@app.route("/read",methods=["GET"])
def read():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    with open("D:\\temp\\BufferFile1".format(directory , file_name), "w+") as file:
        queue:Queue = pickle.load(file)
        if not queue.empty():
            return queue.pop()

# 4.3 Push element to buffer file
@app.route("/update",methods=["POST","PUT","GET","PATCH"])
def update():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    content = request.args.get("content")
    queue = Queue()
    queue.push(content)
    with open("D:\\temp\\BufferFile1".format(directory, file_name), "a+") as file:
        pickle.dump(queue, file)
    return "File has been updated successfully."
'''
# 4.4 Delete buffer file
@app.route("/delete",methods=["DELETE","GET"])
def delete():
    directory = request.args.get("directory")
    file_name = request.args.get("file_name")
    os.remove("D:\\temp\\BufferFile1".format(directory,file_name))
    return "File has been deleted successfully."
'''
if __name__ == "__main__":
    app.run(debug=True)
