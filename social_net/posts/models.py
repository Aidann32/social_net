from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile

class Post(models.Model):
    title=models.CharField(max_length=300)
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts')
    content=models.TextField()
    image=models.ImageField(upload_to='posts/',validators=[FileExtensionValidator(['img','png','jpeg'])],blank=True)
    liked=models.ManyToManyField(Profile,blank=True,related_name='likes')
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_likes_number(self):
        return self.liked.all().count()

    def get_comment_number(self):
        return self.comment_set.all().count()

    class Meta:
        ordering=('-created_at',)

class Comment(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField(max_length=500)
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pk

LIKE_CHOICES=(
    ('Like','Like'),
    ('Unlike','Unlike')
)

class Like(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,max_length=8)
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}:{self.post}:{self.value}"

