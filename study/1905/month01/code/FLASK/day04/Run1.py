from flask import Flask,request,render_template
import datetime
import os
app = Flask(__name__)

@app.route('/upload_file',methods=['GET','POST'])
def upload_file():
    # 根据用户的请求意图去执行不同的功能
    if request.method == "GET":
        return render_template('01-upload.html')
    else:
        username = request.form['username']
        print(username)
        f = request.files['userimage']
        # 获取时间字符串
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        print(ftime)
        # 获取文件的后缀名
        ext = f.filename.split('.')[1]
        print("文件后缀名:{}".format(ext))
        # 拼文件名
        filename = ftime + '.' + ext
        print("文件名称:{}".format(filename))
        # 拼目录
        base_dir = os.path.dirname(__file__)
        upload_path = os.path.join(base_dir,'static/upload',filename)
        print("upload_path:{}".format(upload_path))
        f.save(upload_path)
        return "Upload Success"


if __name__ == '__main__':
    app.run(debug=True)
