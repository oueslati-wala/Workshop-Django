from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import uuid

def generate_user_id():
    return "USER"+uuid.uuid4().hex[:4].upper()
def verify_email(email):
    domaines=["esprit.tn","sesame.com","takup.tn","centrale.net"]
    email_domaine=email.split("@")[1]
    if email_domaine not in domaines:
        raise ValidationError("l'email est invalide et doit appartenir à un domaine universitaire privé")
name_validator=RegexValidator(
    regex=r'^[a-zA-Z\s-]+$',
    message="ce champs ne doit contenir que des lettres et des espaces"
)
class User(AbstractUser):
    user_id=models.CharField(primary_key=True, max_length=8, unique=True,editable=False)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    affiliation=models.CharField(max_length=255)
    ROLE=[
        ("participant","participant"),
        ("organisateur ","organisateur "),
        ("comite","membre du comité scientifique"),
    ]
    role=models.CharField(max_length=255,choices=ROLE,default="participant")
    affiliation=models.CharField(max_length=255)
    nationality=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        if not self.user_id:
            newid=generate_user_id()
            while User.objects.filter(user_id=newid).exists():
                newid=generate_user_id()
            self.user_id=newid
        super().save(*args,**kwargs)