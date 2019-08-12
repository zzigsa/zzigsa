from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from first.models import User
from .models import ProductRegistration
from .forms import *
from django.contrib import auth
from first.models import User,Writer,EmailConfirm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

#작가페이지
def photographer(request,id):
    writer = get_object_or_404(Writer,pk=id)
    # user = get_object_or_404(User, pk=id)
    return render(request,"photographer.html",{ "writer":writer })

#좋아요
def like(request):
    id = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    writer = get_object_or_404(Writer, pk=id)
    writer_like, writer_like_created = writer.like_set.get_or_create(username=request.user)

    if not writer_like_created:
        writer_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': writer.like_count,
               'message': message,
                }

    return HttpResponse(json.dumps(context), content_type="application/json")


# # 상품등록
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
            # if product.writer != request.user.writer:
            #     return render(request,"upload.html" ,{"msg":"작가만 등록이 가능합니다."})
            # else:
            #     product.save()
            #     return redirect('home')
    else:
        form = UploadForm(request.POST, request.FILES)
    return render(request, 'upload.html', {'form': form})

    # if request.method == 'GET':
    #     return render(request, "upload.html")
    # elif request.method == "POST":
    #     title = request.POST['title']
    #     summary = request.POST['summary']
    #     image = request.FILES['image']
    #     detail = request.POST['detail']
    #     options = request.POST['options']
    #     option_price = request.POST['option_price']
    #     product = ProductRegistration.objects.create(
    #         title=title, summary=summary, image=image,
    #         detail=detail, options=options, option_price=option_price
    #     )
    #     if product.user.writer != request.user:
    #         return render(rqeuest,"upload.html" ,{"msg":"작가만 등록이 가능합니다."})
    #     else:
    #         product.save()
    #         return redirect('home')
    #     return redirect('home')


# # 상품 삭제
# def remove_product(request, pk):
#     product = ProductRegistration.objects.get(pk=pk)
#     product.delete()
#     return redirect('/')

# # 상품 수정
# def edit_product(request, pk):
#     product = get_object_of_404(ProductRegistration, pk=pk)
#     if request.method == 'POST':
#         form = UploadForm(instance=product)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.photographer = request.user
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('product_detail', pk=post.pk)
#     else:
#         form = UploadForm(instance=product)
#     return render(request, 'editProduct.html', {'product':product})

def list(request):
    products = ProductRegistration.objects.all()
    list = request.GET.get('list')
    if list:
        products = products.filter(title__contains = list)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, "list.html", {"products":products, "posts":posts})

def photographeredit(request):
    return render(request, "photographeredit.html")