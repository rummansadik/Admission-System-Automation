# Generated by Django 3.2.3 on 2021-06-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
