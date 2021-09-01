from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from .helper import *
# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    content = FroalaField()
    slug     = models.SlugField(max_length=1000,null=True,blank=True)
    created_At = models.DateField(auto_now_add=True)
    user = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate(self.title)
        super(post, self).save(*args, **kwargs)

class profile(models.Model):
    user=OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=1000)
    is_varified=models.BooleanField(default=False)

    

