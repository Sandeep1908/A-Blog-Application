
from keen_project.settings import EMAIL_HOST_USER
from django.utils.text import slugify
import string
import random

from django.conf import settings
from django.core.mail import message, send_mail

def generate_text(N):  
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res


def generate(text):
    from .models import post
    print(text)
    new_slug=slugify(text)
    print(new_slug)
    if post.objects.filter(slug=new_slug).exists():
        return generate(text+generate_text(5))
    return new_slug

  

def send_confirmation(email,token):
    subject=f'Your Account needs to be varified'
    message=f'Hello please click this link to confirmation http://127.0.0.1:8000/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient_list=['sandbro7163337@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    

