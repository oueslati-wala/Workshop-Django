from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from conferenceApp.models import Conference # Assurez-vous que ce modèle a 'start_date' et 'end_date'

# --- Modèle Session ---

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    
    # Le validateur pour session_day est implémenté dans la méthode clean()
    session_day = models.DateField()
    
    # Les validateurs pour les heures sont implémentés dans la méthode clean()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    # 3. room : Utilisation de RegexValidator
    # Regex : ^[a-zA-Z0-9\s]+$ (Lettres, chiffres, et espaces uniquement)
    room = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9\s]+$',
                message="Le nom de la salle ne doit contenir que des lettres, des chiffres et des espaces.",
                code='invalid_room_name'
            )
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="sessions")

    def __str__(self):
        return f"{self.title} ({self.conference.title})"

    def clean(self):
        super().clean()
        conference = self.conference

        if not (conference.start_date <= self.session_day <= conference.end_date):
            raise ValidationError(
                {'session_day': 
                 f"La date de la session doit être entre le {conference.start_date} et le {conference.end_date} (dates de la conférence associée)."}
            )

        if self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                raise ValidationError(
                    {'end_time': "L'heure de fin doit être strictement supérieure à l'heure de début."}
                )