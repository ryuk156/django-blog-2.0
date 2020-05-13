from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
import random
from home.models import homeintro,Books,userpost
# Create your views here.

def home(request):
    userdf=userpost.objects.filter(user=request.user)
    context={'userdf':userdf}
    return render(request,'home/home.html',context)

def home2(request):
    userdf2=userpost.objects.all()
    
    context={'userdf2':userdf2}
    return render(request,'home/home2.html',context)

def search(request):
    query=request.GET['query']
    allpost=Post.objects.filter(title__icontains=query)
    params={'allpost':allpost}
    return render(request,'home/search.html',params)



def about(request):
    return render(request,'home/about.html')




def handlesignup(request):
    if request.method =='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>10:
            messages.error(request,"Username should be less then 10 character")
            return redirect('/')
    

        if not username.isalnum():
            messages.error(request,"Username should should contain letters and number")
            return redirect('/') 

        if pass1!=pass2:
            messages.error(request,"Password didn't match")
            return redirect('/')
            



        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.save()
        messages.success(request,"Your account created successfully")
        return redirect('/')
        

    else:
        return HttpResponse('404-page-not-found')


def  userpage(request):
    return render(request,'user.html')


def handlelogin(request):
    if request.method =='POST':

        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)


        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect('userpage')
        else:
            messages.error(request,"Invalid password and username")
    return HttpResponse('404-page-not-found')




def handlelogout(request):
        logout(request)
        messages.success(request,"Successfully logged out")
        return redirect('userpage')


def user(request):
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        user=request.user
        userposs=userpost(title=title,content=content,user=user)
        userposs.save()
        messages.success(request,"content posted")
    return redirect('userpage')

