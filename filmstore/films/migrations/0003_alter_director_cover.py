# Generated by Django 4.0 on 2022-02-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_document_director_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Фото режиссёра'),
        ),
    ]
