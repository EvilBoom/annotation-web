# Generated by Django 2.2 on 2019-08-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_label', models.IntegerField()),
                ('article_id', models.ForeignKey(on_delete='CASCADE', to='articles.Article')),
            ],
        ),
    ]
