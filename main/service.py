import random
import string
from django.utils import timezone
from .models import Question

def shorten(url):
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Question(original_url = url, hash = random_hash, creatin_date = timezone.now())
    
    mapping.save()
    return random_hash

def load_url(url_hash):
    return Question.objects.get(hash = url_hash)