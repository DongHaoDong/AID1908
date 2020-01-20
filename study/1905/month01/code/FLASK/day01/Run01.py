from flask import Flask,url_for
app = Flask(__name__)

@app.route('/login')
def login():
    return "这是登陆页面"

@app.route('/register')
def register():
    return "这是注册页面"

# 定义带一个参数的路由
@app.route('/show1/<name>')
def show1(name):
    return "<h1>姓名为:{}</h1>".format(name)

# 定义带多个参数的路由
@app.route('/show2/<name>/<age>')
def show2(name,age):
    return "<h1>姓名为:{},年龄为:{}</h1>".format(name,age)

# 定义带来两个参数的路由，其中，age参数指定为整数
@app.route('/show3/<name>/<int:age>')
def show3(name,age):
    # age：为整型，并非字符串
    return "传递进来的参数是name:{},age:{}".format(name,age)

# 多URL路由匹配
@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
@app.route('/index/<int:page>')
def index(page=None):
    if page is None:
        page = 1
    return "当前页数为:{}".format(page)

@app.route('/post',methods=['POST','GET'])
def post():
    return "这是post请求方式进来的"

@app.route('/url')
def url_views():
    # 将login()反向解析访问地址
    # loginUrl = url_for('login')
    # print(loginUrl)
    # resp = "<a href='{}'>我要登录</a>".format(loginUrl)
    # return resp

    # 将show2(name,age)反向解析访问地址
    url = url_for('show2',name='sf.zh',age=85)
    print(url)
    resp = "<a href='{}'>{}</a>".format(url,url)
    return resp
if __name__ == '__main__':
    app.run(debug=True)