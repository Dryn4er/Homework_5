from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_number_of_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='number_of_views',
            field=models.IntegerField(default=0, verbose_name='колличество просмотров'),
        ),
    ]