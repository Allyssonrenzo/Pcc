# Generated by Django 4.2.7 on 2024-08-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('reprovada', 'Reprovada')], default='pendente', max_length=20)),
                ('data_candidatura', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]