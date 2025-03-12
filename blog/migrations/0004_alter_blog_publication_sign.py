from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_number_of_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publication_sign',
            field=models.BooleanField(verbose_name='признак публикации'),
        ),
    ]