from django import forms
from photographer.models import ProductRegistration
from first.models import Writer

# 상품등록
class UploadForm(forms.ModelForm):
    class Meta:
        model = ProductRegistration
        fields = ['title', 'summary', 'image', 'detail', 'options', 'option_price']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-group'}),
            'detail': forms.Textarea(attrs={'class':'form-control'}),
            'options': forms.TextInput(attrs={'class':'form-control'}),
            'option_price': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title': '상품 타이틀',
            'summary': '상품 요약',
            'image': '샘플 사진',
            'detail': '상세 설명',
            'options': '옵션 내용',
            'option_price': '옵션가격',
        }


# 작가 관리
# class PhotographerProfile(forms.ModelForm):
#     class Meta:
#         model = Writer
#         fields = ['profile_image', 'introduce', 'image', 'camera', 'sns_email']
#         widgets = {
#             'profile_image': forms.FileInput(attrs={'class':'form-control'}),
#             'introduce': forms.Textarea(attrs={'class':'form-control'}),
#             'image': forms.FileInput(attrs={'class':'form-control'}),
#             'camera': forms.TextInput(attrs={'class':'form-control'}),
#             'sns_email': forms.URLInput(attrs={'class':'form-control'}),
#         }
#         labels = {
#             'name': '작가 이름',
#             'profile_image': '프로필 사진',
#             'introduce': '작가 소개',
#             'image': '포트폴리오 이미지',
#             'camera': '사용중인 카메라',
#             'sns_email': 'SNS계정',
#         }