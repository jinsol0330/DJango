from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    image = models.CharField(max_length=500, default=None, null=True)
    # 왜 charfield를 썼냐면 여기에 이미지의 url을 넣을거기 때문에 실제로는 문자열로 취급 됨
    password = models.CharField(max_length=20, default=None, null=True)
    # 디폴트 속성을 어떠한 값 이라도 넣어줘야 함
    # 우리가 이미 디폴트 속성을 None 이라고 선언해놨으므로 null값을 허용한다는 선언을 해줘야 함

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
