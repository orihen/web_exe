from flask import Flask, redirect, url_for , render_template, request , session
from intract_with_DB import interact_db
import mysql.connector



app = Flask(__name__)
app.secret_key= '123'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ywa2Znzk!"
)


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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    users = {'user1': {'name': 'Ron', 'age': '27', 'email': 'ron@gmail.com'},
             'user2': {'name': 'Ori', 'age': '30', 'email': 'ori123@gmail.com'},
             'user3': {'name': 'ofir', 'age': '18', 'email': 'fifi@gmail.com'},
             'user4': {'name': 'Shahar', 'age': '23', 'email': 'shahar@gmail.com'},
             'user5': {'name': 'Tali', 'age': '50', 'email': 'tali@gmail.com'}}

    if request.method == 'GET':
        if 'user_key' in request.args:
            if request.args.get('user_key') != '':
                user_key = request.args['user_key']
                for key in users:
                    if key == user_key:
                        user_name = users[key]['name']
                        email = users[key]['email']
                        age = users[key]['age']
                        return render_template('assignment9.html', u_name=user_name, email=email, age=age
                                               )
                return render_template('assignment9.html',not_in='not')
            return render_template('assignment9.html',  users=users)

        return render_template('assignment9.html')



    if request.method == 'POST':
        user_nickname= request.form['user_nickname']
        password= request.form['password']
        found= True
        if found :
            session['user_nickname'] = user_nickname
            session['user_password'] = password
            return render_template('assignment9.html')
        else:
            return render_template('assignment9.html')


@app.route('/logout')
def logout_func():
    session['user_nickname'] = ''
    session['user_password'] = ''
    return render_template('assignment9.html')


## assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)



