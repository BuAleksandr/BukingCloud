from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='comment',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]