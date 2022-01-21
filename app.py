from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from intract_with_DB import interact_db
import mysql.connector
import  requests



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

##assignment11
@app.route('/assignment11/users', methods=['GET'])
def get_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = jsonify(query_result)
    return response


@app.route('/assignment11/outer_source',  methods=['GET', 'POST'])
def assignment11_outer_source():
    return render_template('assignment11/outer_source.html')


@app.route('/outer_source_front', methods=['post'])
def outer_source_front_func():
     user_id = request.form['user_id']
     return render_template('assignment11/outer_source.html', id=user_id)

@app.route('/outer_source_backend')
def req_backend_func():
    if request.args['user_id'] != '':
        id = request.args['user_id']
        res = requests.get('https://reqres.in/api/users/%s' % id)
        user = res.json()
        return render_template('assignment11/outer_source.html', user=user)
    return render_template('assignment11/outer_source.html')


@app.route('/assignment12/restapi_users', defaults ={'user_id': 1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_users_func(user_id):
    query = 'select * from users where id=%s' %user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users)==0:
        return_dict= {
            'status' : 'failed',
            'message' : 'user not found'
        }
    else:
         return_dict= {
            'status' : 'success',
            f'id':users[0].id,
            'name': users[0].name,
            'email': users[0].id,
        }
    return jsonify(return_dict)