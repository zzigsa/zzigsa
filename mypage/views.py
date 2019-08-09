from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib import auth
from first.models import User,Writer,EmailConfirm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from .forms import *


# Create your views here.
#아이디찾기 (비번찾기는 라이브러리 이용)   html안만듬디자인
@login_required
def id_find(request):
    if request.method == "POST":
        name = request.POST["user"]
        email = request.POST["email"]
        find_username = User.objects.filter(name=name, email=email)
        username_length = len(find_username)
        if username_length == 0:
            return render(request, "id_find.html",{"msg":"해당되는 정보가 없습니다."})
        else:
            return render(request, "id_find.html",{"find_username":find_username})
    return render(request, "id_find.html")

#마이페이지
@login_required   
def mypage(request,id):
    people=get_object_or_404(User, pk=id)
    return render(request, "mypage.html",{'people':people})

#정보수정(forms.py에서 수정해야됨)
@login_required
def change_user(request):
    if request.method=='POST':
        form_password = ChangePasswordForm(request.user, request.POST)
        form=UpdateuserForm(request.POST,instance=request.user)
        if form.is_valid() and form_password.is_valid():
            user = form_password.save()
            update_session_auth_hash(request, user)
            form.save()
            return redirect('main')
    else:
        form_password = ChangePasswordForm(request.user)
        form=UpdateuserForm(instance=request.user)
    return render(request,'change_user.html',{'form':form,"form_password":form_password})