# Generated by Django 4.1.1 on 2022-09-19 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudfile',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]