from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_auto_20210512_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quesmodel',
            old_name='ques',
            new_name='question',
        ),
    ]
