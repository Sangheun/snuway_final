from django import forms
from .models import Post
from .widgets import DaumMapWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "vehicle",
            "price",
            "content",
            "latlng",
            'location',
            # 캘린더
        ]
        labels={'title': '제목', 'vehicle':'기기종류', 'price':'가격', 'content': '내용', 'latlng':'대여위치', 'location':'지역 태그'}
        widgets={
            'latlng':DaumMapWidget,
        }


class SearchForm(forms.Form):
    MACHINE_NAME=(
        ('', '전체'),
        ('1', '세그웨이'),
        ('2', '전동 퀵보드'),
        )
    TAG_CHOICES=(
        ('', '전체'),
        ('1', '서울대입구'),
        ('2', '서울대 교내'),
        ('3', '녹두'),
        ('4', '낙성대'),
        )
    machine=forms.ChoiceField(choices=MACHINE_NAME, required=False, label='기기종류')
    location=forms.ChoiceField(choices=TAG_CHOICES, required=False, label='대여지역')
    price=forms.IntegerField(required=False, label='최고가격')

