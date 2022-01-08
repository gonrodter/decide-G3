# Generated by Django 2.0 on 2022-01-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0009_merge_20220108_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='preferences',
            field=models.BooleanField(default=False, help_text='Check for creating a preference question', verbose_name='Preferences'),
        ),
        migrations.AlterField(
            model_name='question',
            name='sino',
            field=models.BooleanField(default=False, help_text='Marcala si quieres que las respuestas genericas sean Si/No. No añadir mas respuesta.'),
        ),
    ]
