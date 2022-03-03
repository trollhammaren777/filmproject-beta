# Generated by Django 4.0 on 2022-02-01 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_column='full_name', max_length=255, verbose_name='Полное имя режиссёра')),
                ('birth_date', models.DateField(db_column='birth_date', verbose_name='Дата рождения')),
                ('age', models.IntegerField(db_column='age', verbose_name='Возраст')),
                ('death_date', models.DateField(db_column='death_date', default='9999-12-31', verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255, unique=True, verbose_name='Название жанра')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=255)),
                ('release_year', models.DateField(db_column='release_year', max_length=255, verbose_name='Год выхода фильма')),
                ('price', models.DecimalField(db_column='price', decimal_places=2, max_digits=19, verbose_name='Цена')),
                ('directors', models.ManyToManyField(related_name='movies', to='films.Director')),
                ('genres', models.ManyToManyField(related_name='movies', to='films.Genre')),
            ],
        ),
    ]