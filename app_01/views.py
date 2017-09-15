# encoding=utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from app_01 import models
from django.views import View

from utils.pager import PageInfo


def session_ok(fn):
    def wrapper(request):
        try:
            user = models.UserInfo.objects.filter(username=request.session['username']).first()
            if user and user.password == request.session['password']:
                return fn(request)
            else:
                return HttpResponseRedirect('/login/')
        except KeyError:
            return HttpResponseRedirect('/login/')
    return wrapper


class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.UserInfo.objects.filter(username=username).first()

        if user and user.password == password:
            request.session['username'] = username
            request.session['password'] = password
            if user.BOY_id == None:
                request.session['name'] = user.GIRL.name
                request.session['sex'] = 'girl'
            else:
                request.session['name'] = user.BOY.name
                request.session['sex'] = 'boy'
            return HttpResponseRedirect('/userinfo/')
        else:
            return HttpResponseRedirect('/login/')
@session_ok
def userinfo(request):
    user = models.UserInfo.objects.filter(username=request.session['username']).first()
    res = render(request, 'userinfo.html', {'user': user})
    return res
@session_ok
def select(request):
    pass
@session_ok
def look(request):
    pass

class Regedit(View):
    def get(self,request):
        return render(request, 'regedit.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')

        db_user = models.UserInfo.objects.filter(username=username).first()
        db_user_1 = models.Boy.objects.filter(name=name).first()
        db_user_2 = models.Girl.objects.filter(name=name).first()
        if(db_user):
            return render(request, 'regedit.html',{'msg_1':'用户名-%s-已存在'%username})
        if(db_user_1 or db_user_2):
            return render(request, 'regedit.html',{'msg_2':'姓名-%s-已存在'%name})
        if sex =='女':
            models.Girl.objects.create(name=name,age=age)
            the_girl = models.Girl.objects.filter(name=name).first()
            models.UserInfo.objects.create(username=username,password=password,GIRL=the_girl)
            request.session['username'] = username
            request.session['password'] = password
            request.session['name'] = name
            request.session['sex'] = 'girl'
        elif sex == '男':
            models.Boy.objects.create(name=name, age=age)
            the_girl = models.Boy.objects.filter(name=name).first()
            models.UserInfo.objects.create(username=username, password=password, BOY=the_girl)
            request.session['username'] = username
            request.session['password'] = password
            request.session['name'] = name
            request.session['sex'] = 'boy'
        return HttpResponseRedirect('/userinfo/')
@session_ok
def engagement(request):
    user = models.UserInfo.objects.filter(username=request.session['username']).first()
    if request.session['sex'] == 'girl':
        user = user.GIRL
        if request.GET.get('girl_name')!=None:
            if request.GET.get('girl_name')==user.name:
                return render(request, 'engagement.html', {'YH_people': '你竟然想和自己约会!'})
            return render(request, 'engagement.html', {'YH_people': '你竟然想和女的约会!'})
        boy_name = request.GET.get('boy_name')
        YH_people = models.Boy.objects.filter(name=boy_name).first()
        user.boy_set.add(YH_people)
    else:
        user = user.BOY
        if request.GET.get('boy_name')!=None:
            if request.GET.get('boy_name')==user.name:
                return render(request, 'engagement.html', {'YH_people': '你竟然想和自己约会!'})
            return render(request, 'engagement.html', {'YH_people': '你竟然想和男的约会!'})
        girl_name = request.GET.get('girl_name')
        YH_people = models.Girl.objects.filter(name=girl_name).first()
        user.B2G.add(YH_people)
    # return HttpResponse('已与%s约会'% YH_people.name)
    return render(request, 'engagement.html',{'YH_people': '已与'+str(YH_people.name)+'约会'})
@session_ok
def boy_list(request):
    boys = models.Boy.objects.all()
    YH_boyList=[]
    if request.session['sex'] == 'girl':
        user = models.UserInfo.objects.filter(username=request.session['username']).first().GIRL
        YH_boyList = [YH_boy['id'] for YH_boy in list(user.boy_set.all().values('id'))]
    page_info = PageInfo(request.GET.get('page'), boys.count(), 10, '/boy_list')
    boyList = boys[page_info.start():page_info.end()]
    return render(request, 'boy_list.html',{'boy_list': boyList,'YH':YH_boyList,'page_info': page_info})
@session_ok
def girl_list(request):
    girls = models.Girl.objects.all()
    YH_girlList=[]
    if request.session['sex'] == 'boy':
        user = models.UserInfo.objects.filter(username=request.session['username']).first().BOY
        YH_girlList = [YH_girl['id'] for YH_girl in list(user.B2G.all().values('id'))]
    page_info = PageInfo(request.GET.get('page'), girls.count(), 10, '/girl_list')
    girlList = girls[page_info.start():page_info.end()]
    return render(request, 'girl_list.html', {'girl_list': girlList, 'YH':YH_girlList, 'page_info': page_info})
@session_ok
def test(request):
    # models.UserInfo.objects.create(username='男孩1',password='123',BOY_id=1)
    # models.UserInfo.objects.create(username='男孩2',password='123',BOY_id=2)
    # models.UserInfo.objects.create(username='男孩3',password='123',BOY_id=3)
    # models.UserInfo.objects.create(username='男孩4',password='123',BOY_id=4)
    # models.UserInfo.objects.create(username='男孩5',password='123',BOY_id=5)
    # models.UserInfo.objects.create(username='女孩1',password='123',GIRL_id=1)
    # models.UserInfo.objects.create(username='女孩2',password='123',GIRL_id=2)
    # models.UserInfo.objects.create(username='女孩3',password='123',GIRL_id=3)
    # models.UserInfo.objects.create(username='女孩4',password='123',GIRL_id=4)
    # models.UserInfo.objects.create(username='女孩5',password='123',GIRL_id=5)
    # for i in range(6,100):
    #     name = '女孩%s' % i
    #     models.Girl.objects.create(name=name,age=18)
    #     models.UserInfo.objects.create(username=name, password='123', GIRL_id=i)
    return HttpResponse('...')