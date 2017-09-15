#from BlogApp import app

from flask_restful import Resource,abort, reqparse
from .__init__ import *
from models import Blogpost,User,Followers
from flask import render_template,jsonify,request
from flask import request,redirect,url_for,session
from datetime import datetime


class UserController(Resource):
    def get(self):
        users=User.objects
        lis=[]
        for a in users:
            lis.append({'uname' :a['uname'],'upass':a['upass']})
        return jsonify({'result':lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('upass')
        args = parser.parse_args()
        user = User(uname=args['uname'], upass=args['upass'])
        user.save()
        return "Success"

class LogInController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('upass')
        args = parser.parse_args()
        one=User.objects(uname=args['uname'],upass=args['upass']).count()
        if one :
            return {'result': args['uname']}
        else:
            return "Sorry"

class BlogpostController(Resource):
    def get(self):
        blgs = Blogpost.objects
        lis = []
        for a in blgs:
            lis.append({'title': a['title'], 'subtitle': a['subtitle']})
        return jsonify({'result': lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uname')
        parser.add_argument('title')
        parser.add_argument('subtitle')
        parser.add_argument('author')
        parser.add_argument('content')
        args = parser.parse_args()
        # a = User.objects(uname=session['username'])
        a = User.objects.get(uname=args['uname'])
        # return render_template('temp.html', myUser=a)
        post = Blogpost(title=args['title'], subtitle=args['subtitle'], author=args['author'], content=args['content'], date_posted=datetime.now(),
                        refuser=a)
        post.save()
        return "Success"

    def delete(self,blog_id):
        Blogpost.objects(id=blog_id).delete()
        return '', 204


    def put(self,blog_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('subtitle')
        parser.add_argument('author')
        parser.add_argument('content')
        args = parser.parse_args()
        blg = Blogpost.objects.get(id=blog_id)
        blg.title = args['title']
        blg.subtitle = args['subtitle']
        blg.author = args['author']
        blg.content = args['content']
        blg.save()
        return  "Success"



class FollowerController(Resource):
    def get(self):
        flws = Followers.objects
        lis = []
        for a in flws:
            lis.append({'followin': a['followin'], 'follower': a['follower']})
        return jsonify({'result': lis})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('followin')
        parser.add_argument('follower')
        args = parser.parse_args()
        print args['followin']
        fin = User.objects.get(id=args['followin'])
        fer = User.objects.get(id=args['follower'])
        post = Followers(followin=fin, follower=fer)
        post.save()
        return "Success"


