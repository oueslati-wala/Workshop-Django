from django.db import models
from userApp.models import User
from conferenceApp.models import Conference

class Committee(models.Model):
    committee_role=models.CharField(primary_key=True,unique=True,editable=False,max_length=50,
                                    choices=[("chair","chair"),("co-chair","co-chair"),("member","memeber")])
    date_joined=models.DateField()

    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="committees")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="committees")