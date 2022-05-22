# Generated by Django 2.2.19 on 2022-05-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20220522_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(help_text='input a description here', max_length=150, verbose_name='Brief description of the item group'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.SlugField(help_text='input a unique url-name of group', unique=True, verbose_name='slug of group'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(help_text='input title here', max_length=150, verbose_name='title of group'),
        ),
    ]
