# Generated by Django 3.2.12 on 2022-03-28 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_alter_board_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['-createdAt']},
        ),
    ]
