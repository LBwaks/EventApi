# Generated by Django 4.1 on 2022-10-03 06:53

from django.db import migrations, models
import django_extensions.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lname',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Bio'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='Town/City'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=50, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='kkk', max_length=50, verbose_name='Full Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profiles/', verbose_name='Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='town',
            field=models.CharField(blank=True, max_length=50, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_artist',
            field=models.CharField(blank=True, max_length=50, verbose_name='Artist Category'),
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_organization',
            field=models.CharField(blank=True, max_length=50, verbose_name='Organisation Category'),
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_user',
            field=models.CharField(default='ii', max_length=50, verbose_name='User Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_venue',
            field=models.CharField(blank=True, max_length=50, verbose_name='Venue Category'),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, verbose_name='Your Website'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]
