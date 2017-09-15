from flask import Flask,session,render_template
from flask_restful import Api,Resource
from mongoengine import *
from flask_cors import CORS
from Blog import views
from Blog.models import *


app = Flask(__name__)
CORS(app)
api = Api(app)
app.secret_key = 'You Will Never Guess'
connect('flask_blog_db',host='mongodb://hiren:hiren@ds133964.mlab.com:33964/flask_blog_db')

api.add_resource(views.UserController, '/api/users')
api.add_resource(views.LogInController, '/api/login')
api.add_resource(views.BlogpostController, '/api/blogs/<blog_id>')
api.add_resource(views.FollowerController, '/api/followers')

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/add_user')
def add_user():
    myUser = User.objects[:]
    return render_template('add_user.html', myUser=myUser)

@app.route('/about')                                        
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    pass