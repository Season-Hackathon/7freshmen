from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_remove_quizmodel_secs'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='totalQues',
            field=models.IntegerField(null=True),
        ),
    ]
