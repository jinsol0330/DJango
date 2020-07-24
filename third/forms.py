from django.forms import ModelForm
from django import forms
from third.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _


REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)  # 리뷰 선택지 정의


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),
            # 리뷰를 달 식당 정보가 사용자에게는 보이면 안됨
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)
            # 선택지를 인자로 전달합니다.
        }
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        # 입력받을 필드를 정의
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'image': _('이미지 url'),
            'password': _('게시물 비밀번호'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
            'image': _('이미지의 url을 입력해주세요.'),
            'password': _('비밀번호를 입력해주세요.'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }  # 사용자 입력 필드에서 비밀번호 입력하는 필드처럼 글자가 가려지는 필드가 나옴
        error_messages = {
            'name': {
                'max_length': _("이름이 너무 깁니다. 30자 이하로 해주세요."),
            },
            'image': {
                'max_length': _("이미지 주소의 길이 너무 깁니다. 400자 이하로 해주세요."),
            },
            'password': {
                'max_length': _("비밀번호가 너무 깁니다. 20자 이하로 해주세요."),
            },
        }


class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']
