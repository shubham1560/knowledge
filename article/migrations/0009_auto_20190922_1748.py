# Generated by Django 2.2.2 on 2019-09-22 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190922_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='use',
        ),
        migrations.DeleteModel(
            name='ArticleView',
        ),
    ]
