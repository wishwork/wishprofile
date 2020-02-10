# Generated by Django 3.0.3 on 2020-02-10 22:32

from django.db import migrations, models
import django.db.models.deletion
import profile.models.media
import profile.models.occupation
import profile.models.organization
import profile.models.profile
import profile.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('anchor', models.CharField(max_length=127, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=60)),
                ('name_fa', models.CharField(max_length=60)),
                ('checked', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('caption', models.TextField(max_length=1000, null=True)),
                ('file', models.FileField(upload_to=profile.models.media.file_upload_location)),
                ('type', models.CharField(choices=[('file', 'file'), ('image', 'image'), ('video', 'video')], max_length=5)),
                ('order', models.FloatField(db_index=True)),
                ('hidden', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to=profile.models.occupation.icon_upload_location)),
                ('name_en', models.CharField(max_length=50)),
                ('name_fa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to=profile.models.profile.picture_upload_location)),
                ('thumbnail', models.ImageField(upload_to=profile.models.profile.thumbnail_upload_location)),
                ('about', models.TextField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=127)),
                ('title_fa', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=60)),
                ('name_fa', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=2000)),
                ('hidden', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.Link')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', related_query_name='recommendation', to='profile.Profile')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='published_recommendations', related_query_name='published_recommendations', to='profile.Profile')),
                ('relationship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.Relationship')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=127)),
                ('name_fa', models.CharField(max_length=127)),
                ('logo', models.ImageField(null=True, upload_to=profile.models.organization.logo_upload_location)),
                ('latitude', models.FloatField(null=True, validators=[profile.validators.latitude])),
                ('longitude', models.FloatField(null=True, validators=[profile.validators.latitude])),
                ('address_en', models.TextField(max_length=1000, null=True)),
                ('address_fa', models.TextField(max_length=1000, null=True)),
                ('phoneNumber', models.CharField(max_length=20, null=True)),
                ('checked', models.BooleanField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('about', models.TextField(max_length=1000, null=True)),
                ('start', models.IntegerField(validators=[profile.validators.year])),
                ('end', models.IntegerField(null=True)),
                ('working', models.BooleanField()),
                ('hidden', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profile.Album')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Organization')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=1000, null=True)),
                ('start', models.IntegerField(validators=[profile.validators.year])),
                ('end', models.IntegerField(null=True, validators=[profile.validators.year])),
                ('grade', models.FloatField(validators=[profile.validators.grade])),
                ('hidden', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profile.Album')),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.Link')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Major')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Organization')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('about', models.TextField(max_length=1000, null=True)),
                ('year', models.IntegerField(null=True, validators=[profile.validators.year])),
                ('order', models.FloatField()),
                ('hidden', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profile.Album')),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.Link')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.Organization')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
    ]