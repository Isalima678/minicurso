# Generated by Django 4.1.2 on 2022-10-20 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpb', '0002_musica_delete_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='dt_lacamento',
            field=models.DateField(blank=True, verbose_name='Lançamento'),
        ),
    ]