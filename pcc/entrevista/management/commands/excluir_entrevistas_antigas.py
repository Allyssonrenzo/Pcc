from django.core.management.base import BaseCommand
from entrevista.models import Entrevista
from django.utils import timezone

class Command(BaseCommand):
    help = 'Exclui entrevistas cuja data já passou'

    def handle(self, *args, **kwargs):
        Entrevista.objects.filter(data__lt=timezone.now().date()).delete()
        self.stdout.write(self.style.SUCCESS('Entrevistas antigas excluídas com sucesso.'))
