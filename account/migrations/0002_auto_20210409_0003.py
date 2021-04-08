# Generated by Django 3.1.7 on 2021-04-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Staff',
            new_name='Curator',
        ),
        migrations.AddField(
            model_name='user',
            name='is_curator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]