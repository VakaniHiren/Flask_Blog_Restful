from flask import Flask,session
from mongoengine import *
from BlogApp.Blog.models import  *

app = Flask(__name__)
app.secret_key = 'You Will Never Guess'
connect('flask_blog_db',host='mongodb://hiren:hiren@ds133964.mlab.com:33964/flask_blog_db')

b=Blogpost.objects
print "Blogs"+str(len(b))

u=User.objects
print "Users :"+str(len(u))
print u
lis=[]
for a in User.objects:
    lis.append(a)
print lis
f=Followers.objects
print "Follows :"+str(len(f))

a = User.objects.get(uname='hiren')
print a.uname

c=Blogpost.objects(refuser=a)
print len(c)

for post in Followers.objects:
    print(post.follower)


lis = Followers.objects(followin='59b7b06adc3132169c7bbc92')
print len(lis)

hire=[]
for a in lis:
  of = User.objects.get(id=a.follower)
  print of.id
  posts = Blogpost.objects(refuser=of)
  hire += posts

print len(hire)

for post in hire:
    print post.title