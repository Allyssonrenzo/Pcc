# Generated by Django 4.2.7 on 2024-08-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('formacao', models.CharField(blank=True, max_length=100, null=True)),
                ('experiencia', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]