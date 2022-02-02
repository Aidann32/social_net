from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.shortcuts import reverse

class ProfileManager(models.Manager):
    def get_all_profiles_to_invite(self,sender):
        profiles=Profile.objects.all().exclude(user=sender)
        profile=Profile.objects.get(user=sender)
        qs=Relationship.objects.filter(Q(sender=profile)|Q(receiver=profile))

        accepted=[]

        for rel in qs:
            if rel.status=='accepted':
                accepted.append(rel.receiver)
                accepted.append(rel.sender)

        available=[profile for profile in profiles if profile not in accepted]

        return available
        
    def get_all_profiles(self,me):
        return Profile.objects.all().exclude(user=me)

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

    objects=ProfileManager()

    def __str__(self):
        return f'{self.user.username}:{self.created_at}'

    __initial_first_name=None
    __initial_last_name=None

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__initial_first_name=self.first_name
        self.__initial_last_name=self.last_name

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

    def get_absolute_url(self):
        return reverse('profiles:profile-detail-view',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        exists=False
        to_slug=self.slug
        if self.first_name!=self.__initial_first_name or self.last_name!=self.__initial_last_name or self.slug=="":
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

class RelationshipManger(models.Manager):

    def invitations_received(self,receiver):
        query_string=Relationship.objects.filter(receiver=receiver,status='send')
        return query_string

class Relationship(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
    status=models.CharField(max_length=8,choices=STATUS_CHOICES)
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)

    objects=RelationshipManger()

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'
