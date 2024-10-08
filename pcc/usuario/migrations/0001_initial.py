# Generated by Django 4.2.7 on 2024-08-15 22:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=30)),
                ('idade', models.IntegerField(default=0)),
                ('endereco', models.CharField(max_length=150)),
                ('sexo', models.CharField(max_length=20)),
                ('deficiencia', models.CharField(blank=True, max_length=100)),
                ('pcd', models.BooleanField(default=False)),
                ('empresaRequiredPermission', models.BooleanField(default=False)),
                ('empresaConfirmPermission', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
