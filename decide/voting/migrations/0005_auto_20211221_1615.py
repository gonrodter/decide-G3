# Generated by Django 2.0 on 2021-12-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_question_sino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='sino',
            field=models.BooleanField(default=False),
        ),
    ]
