from flask import Flask, redirect, url_for , render_template

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/main')
@app.route('/')
def main_func():
    return render_template('cv-main.html')

@app.route('/GetinTouch')
def about_func():
    return render_template('GetinTouch.html')


@app.route('/assignment8')
def assignment8_func():
    return render_template('assignment8.html',
                           profile= {'name': 'Ori','second_name':'Hen'} ,
                           Favorite_song= 'Macarena',
                           hobbies = ('art', 'music', 'animals', 'web')
                           )
