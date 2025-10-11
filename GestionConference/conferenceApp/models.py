from django.db import models

class Conference(models.Model):
    conference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    THEME=[
        ("IA","Computer science & IA"),
        ("SE","science & engineering"),
        ("SC","social science & education"),
        ("ID_Theme","Interdisciplinary Themes")
    ]
    theme=models.CharField(max_length=255,choices=THEME,default="IA")
    location=models.CharField(max_length=255)
    descripption=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    
    #pour avoir une historique à la BD
    created_at=models.DateTimeField(auto_now_add=True) #auto_now_add une seul fois
    update_at=models.DateTimeField(auto_now=True) #auto_now atoute modifications
    def clean(self):
        if self.start_date > self.end_date:
            raise ValueError("la date de debut de la conference doit etre  antérieur à la date fin")
    def __str__(self):
        return f"le id est: {self.conference_id}"
