from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib import auth
from .models import User,Writer,EmailConfirm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
#이메일 관련된 라이브러리
from django.core.mail import send_mail
from .hash_generator import generate_random_string

# Create your views here.

#메인(작가페이지 테스트(메인만))
def home(request):
    return render(request, "home.html")

#로그인
def customer_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            # return login_next(request, user)
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'customer_login.html', {'form': form})

#회원가입
def join(request):
    if request.method == "GET":
        return render(request, "join.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_check = request.POST["password_check"]
        name = request.POST["user"]
        email = request.POST["email"]
        if User.objects.filter(username=username).exists():
            return render(request, "join.html",{"msg":"이미 존재하는 ID입니다."})
        if password != password_check:
            return render(request, "join.html",{"pw_msg":"비빌번호가 일치하지않습니다."})
        user = User.objects.create_user(
            username=username, password=password, name=name,
             email=email)
        user.save()        
        return login_next(request, user)


#작가등록(모델 하나아직)
@login_required
def enroll(request, id):
    if request.method == "GET":
        writer_account =  get_object_or_404(User, pk=id, is_active=True)
        return render(request, "enroll.html",{"writer_account":writer_account})
    elif request.method == "POST":
        introduce = request.POST["introduce"]
        profile_image = request.FILES["profile_image"]
        image = request.FILES["image"]
        sns_email = request.POST["sns_email"]
        camera = request.POST["camera"]
        camera_image = request.FILES["camera_image"]
        writer_account =  get_object_or_404(User, pk=id, is_active=True)
        writer_user = Writer.objects.create(introduce=introduce, profile_image=profile_image,
            camera=camera, camera_image=camera_image,sns_email=sns_email, image=image)
        writer_account.is_active = False
        writer_account.writer = writer_user
        writer_account.save()
        # login(request,writer_account)
    return redirect("home")

    
#로그아웃
def signout(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            auth.logout(request)
    return redirect('home')

#이메일전송
def send_confirm_mail(user):
    try:
        email_confirm = EmailConfirm.objects.get(user=user)
    except EmailConfirm.DoesNotExist:
        email_confirm = EmailConfirm.objects.create(
            user = user,
            key = generate_random_string(length=60),
        )
    url = '{0}{1}?key={2}'.format(
        'http://localhost:8000',
        reverse('confirm_email'),
        email_confirm.key,
    )
    html = '<p>계속하시려면 아래 링크를 눌러주세요.</p><a href="{0}">인증하기</a>'.format(url)
    send_mail(
        '인증 메일입니다.',
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=html,
    )

#이메일보냇습니다 html
def email_sent(request):
    return render(request, "email_sent.html")

def confirm_email(request):
    key = request.GET.get('key')
    try:
        email_confirm = get_object_or_404(EmailConfirm, key=key, is_confirmed=False)
        email_confirm.is_confirmed = True
        email_confirm.save()
        return redirect(reverse('home'))
    except:
        return render(request, 'customer_login.html')


#이메일 전송
def login_next(request, user):
    if EmailConfirm.objects.filter(user=user, is_confirmed=True).exists():
        auth.login(request, user)
        return redirect(reverse('home'))
    else:
        send_confirm_mail(user)
        return redirect(reverse('email_sent'))

def bestphoto(request):
<<<<<<< HEAD
    return render(request, "bestphoto.html")

def recommend(request):
    return render(request, "recommend.html")
=======
    return render(request,'bestphoto.html')

def recommend(request):
    return render(request,'recommend.html')
>>>>>>> 82f4b21d96c5f5d204b295379410cdd20b705d30
