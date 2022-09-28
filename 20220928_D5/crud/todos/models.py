from django.db import models

# Create your models here.
class Todo(models.Model):
    # 장고는 pk 자동 생성
    content = models.CharField(max_length=80)
    # default = 내용이 없으면 이걸로 넣어줘
    completed = models.BooleanField(default=False)
    # priority = models.IntegerField(default=3)
    # created_at = models.DateField(auto_now_add=True)
    # deadline = models.DateField(null=True)
