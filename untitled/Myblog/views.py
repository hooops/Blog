from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from models import User
import models
from django.contrib.sessions.models import Session
from models import Category,Blog_user
from django.contrib import comments
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import socket
def acc_login(request):
 try:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        content = '''
        Welcome %s !!!
        
        <a href='/logout/' >Logout</a>
        
         ''' % user.username
        #return HttpResponse(content)

        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
    
 except:
     return HttpResponse('ERROR 0001')#0001

def logout_view(request):
 try:
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    # return HttpResponse("<b>%s</b> logged out! <br/><a href='/index/'>Re-login</a>" % user)
    return index(request)
 except:
     return HttpResponse('ERROR 0002')#0002

def Login(request):
 try:
    return render_to_response('login.html')
 except:
     return HttpResponse('ERROR 0003')#0003



def index(request):
 try:
    # blog_list = models.Blog.objects.all()
    blog_list = models.Blog.objects.order_by('-id').all()

    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html', {
                                             'blog_list':blog_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})
 except:
     return HttpResponse('ERROR 0004')#0004


def category(request,cata_id):
 try:
    bbs_list = models.Blog.objects.filter(category__id=cata_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',
                               {'bbs_list':bbs_list,
                                 'user':request.user,
                                 'bbs_category':bbs_categories,
                                 'cata_id': int(cata_id),
                              })

 except:
     return HttpResponse('ERROR 0005')#0005

def bbs_detail(request, bbs_id):
 # try:
    bbs = models.Blog.objects.get(id=bbs_id)
    print '--->', bbs
    user=models.Blog.objects.get(id=bbs_id)
    usert=User.objects.get(id=user.author_id)
    return render_to_response('blog_detail.html', {'blog_obj':bbs,'user':request.user,'username_':usert})
 # except:
 #    return HttpResponse('ERROR 0006')#0006
    
def sub_comment(request):
 try:
    print  request.POST
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')
    
    if comment is not None:
        hostname=socket.gethostname()
        ip=socket.gethostbyname(hostname)

        comments.models.Comment.objects.create(
            content_type_id = 7,
            object_pk= bbs_id,
            site_id = 1,
            user = request.user,                       
            comment =   comment,
            ip_address=ip,
                                   )
        return  HttpResponseRedirect('/detail/%s' % bbs_id)
    else:
        return  HttpResponseRedirect('/detail/' )


 except:
     return HttpResponse('ERROR 0007')#0007

def bbs_sub(request):
 try:
    print ',==>', request.POST.get('content')
    title=  request.POST.get('title')
    content=  request.POST.get('content')
    # category=request.user.blog_user.user_id
    # author = models.Blog_user.objects.get(user__username=request.user)
    author = models.Blog_user.objects.get(user__username=request.user)
    # author = models.Blog_user.objects.get(user__username=request.user)
    # category_id = models.Blog_user.objects.get(category_id=category)
    # authorid=author.user_id
    # authorid=models.Category.objects.get(administrator_id=author.id)
    # author_id = models.Blog_user.objects.get(user__username=request.user)
    category = request.POST.get('category_id')
    # print 'user_id_'
    # print user_id_
    # user = request.user
    # print '1'
    # print user.blog_user.user_id
    # category=  request.POST.get('category_id')
    # models.Blog_user.objects.create(
    #     # name=title,
    #     user_id=user.blog_user.user_id,
    #
    # )
    models.Blog.objects.create(
        title = title,
        summary = 'github',
        content = content,
        author =author,
        view_count= 1,
        ranking = 1,
        category_id=category,
           )

    return index(request)
 except:
     return HttpResponse('ERROR 0008')#0008
def bbs_pub(request):
 # try:
    # bbs_categories = models.Category.objects.all()
    author = models.Blog_user.objects.get(user__username=request.user)
    category_ids=models.Category.objects.all()
    category_id=[]
    for s in category_ids:
        category_id.append(s)
        print category_id
    # category_id2=category_id
    # category=  request.POST.get('category')
    # models.Category.objects.create(
    #     name=category,
    #     administrator_id=author,
    #
    # )
    return render_to_response('bbs_pub.html',{'category_id':category_id})
    # t= loader.get_template('bbs_pub.html')
    # c=Context({'category_id':category_id})
    # return HttpResponse(t.render(c))
 # except:
 #     return HttpResponse('ERROR 0009')#0009

def delete(request):
     blog_id=request.POST.get('blog_id')
     p=models.Blog.objects.get(id=blog_id)
     p.delete()
     blog_list = models.Blog.objects.all()
     bbs_categories = models.Category.objects.all()
     return render_to_response('index.html', {
                                             'blog_list':blog_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})

def bianji(request):


    author = models.Blog_user.objects.get(user__username=request.user)
    category_ids=models.Category.objects.all()
    blog_id=request.POST.get('blog_id')
    p=models.Blog.objects.get(id=blog_id)
    category_id=[]
    for s in category_ids:
        category_id.append(s)
        print category_id

    return render_to_response('bbs_bianji.html',{'category_id':category_id,'p':p})

def bbs_bianji(request):
 try:
    print ',==>', request.POST.get('content')
    title=  request.POST.get('title')
    content=  request.POST.get('content')
    blog_id=request.POST.get('blog_id')
    # category=request.user.blog_user.user_id
    # author = models.Blog_user.objects.get(user__username=request.user)
    author = models.Blog_user.objects.get(user__username=request.user)
    # author = models.Blog_user.objects.get(user__username=request.user)
    # category_id = models.Blog_user.objects.get(category_id=category)
    # authorid=author.user_id
    # authorid=models.Category.objects.get(administrator_id=author.id)
    # author_id = models.Blog_user.objects.get(user__username=request.user)
    category = request.POST.get('category_id')
    # print 'user_id_'
    # print user_id_
    # user = request.user
    # print '1'
    # print user.blog_user.user_id
    # category=  request.POST.get('category_id')
    # models.Blog_user.objects.create(
    #     # name=title,
    #     user_id=user.blog_user.user_id,
    #
    # )
    p=models.Blog.objects.get(id=blog_id)
    p.title = title
    p.summary = 'github'
    p.content = content
    p.author =author
    p.view_count= 1
    p.ranking = 1
    p.category_id=category
    p.save()


    return index(request)
 except:
     return HttpResponse('ERROR 0008')#0008

def zhucesave(request):
 try:
    username=request.POST.get('username')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')

    if username and password is not None:

        models.User.objects.create(
             username=username,
            password=make_password(password,None,'pbkdf2_sha256'),
            first_name=first_name,
            last_name=last_name,
            email=email,)
        s=models.User.objects.get(username=username)

        models.Blog_user.objects.create(
        signature='This guy is too lazy to levave anything here.',
        user_id=s.id)





        blog_list = models.Blog.objects.all()
        bbs_categories = models.Category.objects.all()
        return render_to_response('index.html', {
                                             'blog_list':blog_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})


    else:
        return HttpResponse('password and uasename is not None~~')
 except:
        return HttpResponse('ERROR 0009')#0009

def ziliao(request):
    return render_to_response('user.html')

def zhuce(request):
    return render_to_response('user.html')

def deletepin(request):
    pin_id=request.POST.get('pin_id')
    p=comments.models.Comment.objects.get(id=pin_id)


    p.delete()
    return HttpResponse('ok')
    # return bbs_detail(request, pin_id)
