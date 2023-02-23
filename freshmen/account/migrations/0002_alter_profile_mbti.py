# Generated by Django 4.1.6 on 2023-02-24 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ENFP', 'ENFP'), ('ESFJ', 'ESFJ'), ('INTP', 'INTP'), ('ENTP', 'ENTP'), ('INFJ', 'INFJ'), ('INTJ', 'INTJ'), ('ENFJ', 'ENFJ'), ('ISFP', 'ISFP'), ('ESTJ', 'ESTJ'), ('ISFJ', 'ISFJ'), ('INFP', 'INFP'), ('ESFP', 'ESFP'), ('ENTJ', 'ENTJ'), ('ISTJ', 'ISTJ'), ('ISTP', 'ISTP'), ('ESTP', 'ESTP')], max_length=16, null=True),
        ),
    ]