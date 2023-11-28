from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_alter_filemodel_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='filemodel',
            unique_together=set(),
        ),
    ]