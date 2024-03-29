# Generated by Django 2.2.4 on 2019-10-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20191001_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=10)),
                ('l_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('tel_no', models.BigIntegerField(blank=True, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('other', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
