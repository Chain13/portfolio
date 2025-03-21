# Generated by Django 5.1.7 on 2025-03-19 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Video'), ('code', 'Code'), ('separator', 'Separator')], max_length=20)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('video', models.URLField(blank=True, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='core.blog')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
