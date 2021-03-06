# Generated by Django 3.1.3 on 2020-11-06 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_mature', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=300)),
                ('path', models.CharField(max_length=60)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_down', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_down', models.IntegerField(default=0)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Audio.audio')),
            ],
        ),
    ]
