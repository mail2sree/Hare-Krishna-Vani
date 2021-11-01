from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Live(models.Model):
    live_url = models.CharField(max_length=2090)

class Prabhu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=60)
    image = models.CharField(max_length=900)
    description = models.TextField(max_length=9000)
    is_there_in_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=900)
    date = models.DateTimeField(auto_now=False)
    youtube_video_link = models.CharField(max_length=900)
    picture = models.CharField(max_length=8000)

class TempleKirtan(models.Model):
    title = models.CharField(max_length=800)
    song_url = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title

class FestivalTrack(models.Model):
    title = models.CharField(max_length=800)
    song_url = models.FileField(upload_to='songs/')

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an usernme')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, password, email):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            last_name=last_name,
            first_name=first_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = MyAccountManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class Content(models.Model):
    prabhu = models.ForeignKey(Prabhu, on_delete=models.CASCADE)
    name = models.CharField(max_length=9000)
    image = models.CharField(max_length=900000)

    def __str__(self):
        return f'{self.prabhu}, {self.name}'

class Audio(models.Model):
    prabhu = models.ForeignKey(Content, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    song = models.FileField(upload_to='songs/')

class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    song_1 = models.ForeignKey(Audio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Notification(models.Model):
    title = models.CharField(max_length=900)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000)
    live_link = models.CharField(max_length=9000, blank=True)

class Ratings(models.Model):
    subject = models.CharField(max_length=900, default='(no subject)')
    rating_content = models.TextField(max_length=9000)