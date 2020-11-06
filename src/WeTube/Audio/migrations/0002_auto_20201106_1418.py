# Generated by Django 3.1.3 on 2020-11-06 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Audio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_down', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='audiocomment',
            name='audio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Audio.audio'),
        ),
        migrations.AddField(
            model_name='audiocomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
