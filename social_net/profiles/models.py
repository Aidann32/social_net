from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify

class Profile(models.Model):
    first_name=models.CharField(max_length=200,blank=True)
    last_name=models.CharField(max_length=200,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(default='Биографии нету',max_length=300)
    email=models.EmailField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    avatar_image=models.ImageField(default='avatar.png',upload_to='avatars/')
    friends=models.ManyToManyField(User,blank=True,related_name='friends')
    slug=models.SlugField(unique=True,blank=True)
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}:{self.created_at}'

    def get_friends(self):
        return self.friends.all()
    
    def get_friends_number(self):
        return self.friends.all().count()

    def get_posts_number(self):
        return self.posts.all().count()
    
    def get_all_author_post(self):
        return self.posts.all()
        
    def get_given_likes_number(self):
        likes=self.like_set.all()
        total_liked=0
        for i in likes:
            if i.value=='Like':
                total_liked+=1
        return total_liked

    def get_received_likes_number(self):
        posts=self.posts.all()
        total_liked=0
        for i in posts:
            total_liked+=i.liked.all().count()
        return total_liked

    def save(self,*args,**kwargs):
        exists=False
        if self.first_name and self.last_name:
            to_slug=slugify(str(self.first_name)+' '+str(self.last_name))
            exists=Profile.objects.filter(slug=to_slug).exists()
            while exists:
                to_slug=slugify(to_slug+' '+str(get_random_code()))
                exists=Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug=str(self.user)
        self.slug=to_slug
        super().save(*args,**kwargs)

STATUS_CHOICES=(
    ('send','send'),
    ('accepted','accepted'),
)
class Relationship(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status=models.CharField(max_length=8,choices=STATUS_CHOICES)
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'
