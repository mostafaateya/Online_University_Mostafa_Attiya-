# Generated by Django 3.0.8 on 2020-12-15 11:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20201215_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='old_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Accordion',
        ),
        migrations.AddField(
            model_name='curriculam',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acc_posts', to='posts.Post'),
        ),
    ]
