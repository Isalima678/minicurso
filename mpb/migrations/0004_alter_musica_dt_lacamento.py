# Generated by Django 4.1.2 on 2022-10-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpb', '0003_alter_musica_dt_lacamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='dt_lacamento',
            field=models.DateField(blank=True, null=True, verbose_name='Lançamento'),
        ),
    ]
