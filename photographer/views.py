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
    return render(request, 'upload.html')
# def Upload(request):
#     if request.method == 'GET':
#         form = UploadForm(request.POST, request.FILES)
#         return render(request, ".html", {"form": form})
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.photographer = request.user
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('product_detail', pk=post.pk)
#     return render(request, '.html')

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