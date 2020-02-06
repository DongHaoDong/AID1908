from flask import Flask,render_template,request,make_response,redirect
app = Flask(__name__,template_folder='t',static_url_path='/s',static_folder='s')
@app.route('/')
def index():
    return render_template('01-index.html')
@app.route('/request')
def request_views():
    # 将request中的成员打印在终端上
    # print(dir(request))
    # 获取请求方案(协议)
    scheme = request.scheme
    # 获取强求方式
    method = request.method
    # 获取get请求提交的数据
    args = request.args
    # 获取post请求提价的数据
    form = request.form
    # 任意一种请求方式提交的数据
    values = request.values
    # 获取cookies
    cookies = request.cookies
    # 获取path(请求路径)
    path = request.path
    # 获取headers(请求消息头)
    headers = request.headers
    # 获取headers中的User-Agent请求消息头
    ua = request.headers['User-Agent']
    # 获取headers中的referer请求消息头:请求源地址
    referer = request.headers.get('referer','')
    # 获取请求的完整路径
    full_path = request.full_path
    # 获取访问地址
    url = request.url

    return render_template('02-request.html',params=locals())
@app.route('/form')
def form_views():
    return render_template("03-form.html")
@app.route('/form_do')
def form_do():
    if request.method == 'GET':
        # 获取form表单提交的数据
        username = request.args.get('username')
        password = request.args.get('password')
        print("用户名称{},用户密码{}".format(username,password))
    return "获取表单数据成功!"
@app.route('/post',methods=['post','GET'])
def post():
    if request.method == "GET":
        return render_template('04-form.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        trueName = request.form.get('trueName')
        print("姓名:{},密码{},邮件:{},真实姓名{}".format(username, password, email, trueName))
        # return "Post Ok"
        # 重定向到'/'首页
        return redirect('/')
@app.route('/response')
def response_views():
    # 响应普通字符串给客户端-使用响应对象
    # 创建响应对象，并赋值响应的字符串
    # resp = make_response('使用响应对象响应回去的内容')
    # 创建响应对象，并赋值响应的模板
    resp = make_response(render_template('04-form.html'))
    # 将响应对象进行返回
    return resp
@app.route('/file',methods=['POST','GET'])
def file_views():
    if request.method == 'GET':
        return render_template('05-file.html')
    else:
        # 接收名称为userimage的图片(文件)
        f = request.files['userimage']
        # 获取上传的图片名称
        filename = f.filename
        print("文件名称:{}".format(filename))
        # 再将图片保存到指定路径(static)
        f.save('S/'+filename)
        return "Upload OK"

if __name__ == '__main__':
    app.run(debug=True)
