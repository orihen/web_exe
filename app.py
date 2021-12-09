from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_func():
    return 'Hello World!'

@app.route('/catalog')
def catalog_func():
    return 'Welcome to catalog Page'

@app.route('/about')
def about_func():
    return redirect('/catalog')

@app.route('/contact')
def contact_func():
    return redirect(url_for('hello_func'))


if __name__ == '__main__':
    app.run(debug=True)
