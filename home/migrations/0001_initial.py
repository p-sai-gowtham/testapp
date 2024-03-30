# Generated by Django 5.0.1 on 2024-02-27 15:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem_Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_statement', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_statement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('problem_statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='home.problem_statement')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
