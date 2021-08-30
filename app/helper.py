
from django.utils.text import slugify
import string
import random
  

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

  