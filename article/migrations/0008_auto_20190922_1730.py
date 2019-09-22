# Generated by Django 2.2.2 on 2019-09-22 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190922_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField()),
                ('views', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='use',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.ArticleView'),
        ),
    ]
