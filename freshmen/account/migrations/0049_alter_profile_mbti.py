# Generated by Django 3.2.17 on 2023-02-24 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0048_auto_20230224_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ESTJ', 'ESTJ'), ('INTP', 'INTP'), ('ISFJ', 'ISFJ'), ('INTJ', 'INTJ'), ('ESFP', 'ESFP'), ('ENTJ', 'ENTJ'), ('ESTP', 'ESTP'), ('ISTJ', 'ISTJ'), ('ISFP', 'ISFP'), ('INFJ', 'INFJ'), ('INFP', 'INFP'), ('ENFP', 'ENFP'), ('ESFJ', 'ESFJ'), ('ENTP', 'ENTP'), ('ISTP', 'ISTP'), ('ENFJ', 'ENFJ')], max_length=16, null=True),
        ),
    ]
