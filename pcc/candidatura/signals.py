from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Candidatura
from entrevista.models import Entrevista

@receiver(post_save, sender=Candidatura)
def delete_interviews_on_status_change(sender, instance, created, **kwargs):
    if not created and instance.status in ['aprovada', 'reprovada']:
        Entrevista.objects.filter(candidatura=instance).delete()
