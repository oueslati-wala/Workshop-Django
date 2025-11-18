from django.db import models
from userApp.models import User
from conferenceApp.models import Conference
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.db.models import Count
import uuid
def validate_max_keywords(value, max_keywords=10):
    keywords_list=[k.strip() for k in value.split(',') if k.strip()]
    if len(keywords_list)>max_keywords:
        raise ValidationError(
            f"Vous ne pouvez soumettre qu'un maximum de {max_keywords} mots-clés. Vous en avez {len(keywords_list)}.",
                code='max_keywords'
        )

class Submission(models.Model):
    submission_id=models.CharField(primary_key=True,unique=True,editable=False,max_length=255)
    title=models.CharField(max_length=50)
    abstract=models.TextField()
    keywords=models.TextField(validators=[validate_max_keywords])
    paper=models.FileField(
                            upload_to="papers/",
                           validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
                           )
    STATUS=[
        ("submitted","submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    ]
    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateField(auto_now_add=True)

    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="submission")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submission")
    def __str__(self):
        return f"{self.submission_id} - {self.title}"
    def clean(self):
        
        super().clean()

        # 1. La Soumission ne peut être faite que pour des conférences à venir
        # (Hypothèse : Conference a un champ 'start_date' ou 'end_date')
        if self.conference.end_date < timezone.now().date():
             raise ValidationError(
                {'conference': "La soumission n'est pas possible pour une conférence déjà terminée."}
             )
        
        # 2. Limiter le nombre de soumissions par jour (ex: 3 max par jour)
        
        # Date d'aujourd'hui
        today = timezone.now().date()
        
        # Compter les soumissions de cet utilisateur faites aujourd'hui
        # Exclure l'objet actuel si on est en train de le modifier
        submission_count = Submission.objects.filter(
            user=self.user,
            submission_date=today
        ).exclude(pk=self.pk).count()

        MAX_SUBMISSIONS_PER_DAY = 3
        
        if submission_count >= MAX_SUBMISSIONS_PER_DAY:
            raise ValidationError(
                {'user': f"Vous avez atteint la limite de {MAX_SUBMISSIONS_PER_DAY} soumissions par jour."}
            )

    def save(self, *args, **kwargs):
        
        if not self.submission_id:
            # Générer un identifiant unique de 8 caractères hexadécimaux
            unique_id = uuid.uuid4().hex[:8].upper()
            self.submission_id = f"SUB-{unique_id}"
            
        # Appeler la méthode parente avant la validation
        super().save(*args, **kwargs)