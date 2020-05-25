from django.db import models

# Create your models here.

class = Article (models.Model):
    title = models. CharField(max_length=30)
    content = models. TextField()
    due_date = models. DateTimeField()

    # DateTimeField는 오류 뜰 수 있으니 수정해야할 가능성 높음

def __str__(self): 
    return self.title

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

# ForeignKey 이해...... 아래 설명시 뭐가 같이 삭제된다는거지?
# "on delete cascade"는 B tuple이 foreign key로 A tuple을 가리키고 있을 때, A tuple을 삭제하면 B tuple도 같이 삭제되는 기능이다. 

