from flask import Flask,render_template
app = Flask(__name__)

@app.route('/index')
def index():
    str = render_template('index.html')
    return str

if __name__ == '__main__':
    app.run(debug=True)