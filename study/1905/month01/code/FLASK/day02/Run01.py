from flask import Flask,render_template
app = Flask(__name__)
class Person(object):
    def say(self):
        name = None
        return "hello I'm a person"
@app.route('/temp')
def temp():
    # dict_bookInfo = {
    #     'title':'我的第一个模板',
    #     'bookName':'钢铁是怎样炼成的',
    #     'author':'奥斯特洛夫斯基',
    #     'price':32.5,
    #     'publisher':'北京大学出版社'
    # }
    title = '我的第一个模板'
    bookName = '钢铁是怎样炼成的'
    author = '奥斯特洛夫斯基'
    price = 32.5
    publisher = '北京大学出版社'
    list01 = ["金毛狮王","青翼蝠王","白眉鹰王","紫衫龙王"]
    tuple01 = ('刘德华','张学友','黎明','郭富城')
    dic = {
        'LW':'魏明泽',
        'WWC':'王伟超',
        'LZ':'吕泽',
        'MM':',萌萌',
        'PY':'皮爷',
    }
    person = Person()
    person.name = '董浩东'
    uname = 'hello world'
    return render_template('01_temp.html',params=locals())

@app.route('/login')
def login():
    return '这里是登录页面'

@app.route('/index')
def index():
    return render_template('03_index.html',uname="测试变量")

@app.route('/parent')
def parent():
    return render_template('04_parent.html')

@app.route('/child')
def child():
    return render_template('05_child.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
if __name__ == '__main__':
    app.run(debug=True)

