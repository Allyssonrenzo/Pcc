# Generated by Django 4.2.7 on 2024-08-15 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('candidatura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('candidatura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidatura.candidatura')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
            ],
        ),
    ]
