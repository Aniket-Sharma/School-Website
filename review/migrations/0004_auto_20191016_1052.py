# Generated by Django 2.2.6 on 2019-10-16 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_contact_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
