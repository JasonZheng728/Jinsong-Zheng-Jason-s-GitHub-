from flask import Flask,request,send_from_directory, render_template, send_file
import os
import shutil

app = Flask(__name__)

#@app.route('/')
#def home():
#    return render_template("FileOperation.html")

root_dir2 = r'D:\temp\root_dir2\sub_dir22\sub_dir222'
root_dir5 = r'D:\temp\root_dir5\sub_dir55\sub_dir555'
root_dir7 = r'D:\temp\root_dir7\sub_dir77\sub_dir777'
root_dir9 = r'D:\temp\root_dir9\sub_dir99\sub_dir999'

# 1.1 Create directory
@app.route('/')
def index():
    files = os.makedirs(root_dir2)
    files = os.makedirs(root_dir5)
    files = os.makedirs(root_dir7)
    files = os.makedirs(root_dir9)
'''
# 1.2 Delete directory
@app.route('/')
def index():
    files = os.rmdir(root_dir2)
    # files = os.rmdir('D:\\temp\\root_dir2\\sub_dir22\\sub_dir222'
'''
# 1.3 List files and subdirectories
root_dir = r'D:\temp'
@app.route('/')
def index():
    files = os.listdir(root_dir)
    isdir_list = gen_isdir_list(root_dir)
    return render_template("files_list.html", files=files, isdir_list=isdir_list)

@app.route('/<path:sub_dir>')
def sub_dir1_page(sub_dir):
    dir_name = root_dir + '\\' + sub_dir
    files = os.listdir(dir_name)
    isdir_list = gen_isdir_list(dir_name)
    return render_template("files_list.html", files=files, isdir_list=isdir_list)

@app.route('/<path:sub_dir1>/<path:sub_dir2>')
def sub_dir2_page(sub_dir1, sub_dir2):
    dir_name = root_dir + '\\' +sub_dir1 + '\\' + sub_dir2
    files = os.listdir(dir_name)
    isdir_list = gen_isdir_list(dir_name)
    return render_template("files_list.html", files=files, isdir_list=isdir_list)

@app.route('/<filename>')
def download_root(filename):
    return send_from_directory(root_dir,filename)

@app.route('/<path:sub_dir>/<filename>')
def download_subdir1(sub_dir, filename):
    dir_name = root_dir + "\\" + sub_dir
    return send_from_directory(dir_name, filename)

@app.route('/<path:sub_dir1>/<path:sub_dir2>/<filename>')
def download_subdir2(sub_dir1, sub_dir2, filename):
    dir_name = root_dir + '\\' + sub_dir1 + '\\' + sub_dir2
    return send_from_directory(dir_name, filename)

def gen_isdir_list(dir_name):
    files = os.listdir(dir_name)
    isdir_list = []
    for f in files:
        if os.path.isdir(dir_name + '\\' + f):
            isdir_list.append(True)
        else:
            isdir_list.append(False)
    return isdir_list

# 1.4 Move file or subdirectory to another location
def index():
    shutil.move('D:\\temp\\root_dir9\\sub_dir99\\sub_dir999','D:\\temp\\root_dir7\\sub_dir77\\sub_dir777')

if __name__ == "__main__":
    app.run(debug=True)
