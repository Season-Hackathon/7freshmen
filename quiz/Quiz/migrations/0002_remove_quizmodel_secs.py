from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmodel',
            name='secs',
        ),
    ]
