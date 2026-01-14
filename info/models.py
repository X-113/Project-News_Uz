import datetime
from .auth_models import User

from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=56)
    slug = models.SlugField(max_length=56, null=True)
    is_menu = models.BooleanField(default=False, verbose_name="Menyuda chiqsinmi?")

    def response(self, ctg_one=False):
        natija = {
            "id":self.id,
            "name":self.name,
            "slug":self.slug,
            "is_menu": "Saytda Chiqadi" if self.is_menu else "Chiqmaydi"
        }
        if ctg_one:
            natija['news'] = [new.ctg_response() for new in self.news.all().order_by('-id')]

        return natija

        

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

class New(models.Model):
    title = models.CharField(max_length=512)
    tags = models.CharField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news")
    short_desc = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="news/")
    created = models.DateTimeField(auto_now_add = True)
    views = models.IntegerField(default=0, editable=False)

    def ctg_response(self):
        natija = {
            "title": self.title,
            "tags": self.tags,
            "short_description": self.short_desc,
            "views": self.views,
            "date": self.get_date()
        }
        if self.image:
            natija['main_image'] = f"http://127.0.0.1:8000{self.image.url}"

        if self.images.all():
            natija['images'] = [f"http://127.0.0.1:8000{i.img.url}" for i in self.images.all()]

        return natija


    def increase_view(self):
        self.views += 1
        self.save()


    def get_tags(self):
        return self.tags.strip('#').split('#')


    def get_desc(self):
        return self.description.split("\n")

    def get_short(self):
        return self.short_desc.split("\n")


    def save(self, *args, **kwargs):
        if "#" not in self.tags:
            self.tags = "#" + " #".join(self.tags.split())
        return super(New, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    def get_date(self):
        now = datetime.datetime.now()
        minut = int((now - self.created).total_seconds() // 60)
        if minut < 2:
            return "Hozirgina"
        if 2 <= minut < 60:
            return f"{minut} minut oldin"

        if 60 <= minut < 24 * 60:
            return f"{int(minut // 60)} soat oldin"
        return self.created.strftime('%H:%M | %d.%m.%Y')


class NewsImage(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name="images")
    img = models.ImageField(upload_to="news/")


class Comment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', null=True, blank=True)
    user = models.CharField(max_length=128)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_sub = models.BooleanField(default=False)
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user} | {self.message}"

    def get_date(self):
        now = datetime.datetime.now()
        minut = int((now - self.created).total_seconds() // 60)
        if minut < 2:
            return "Hozirgina"
        if 2 <= minut < 60:
            return f"{minut} minut oldin"

        if 60 <= minut < 24 * 60:
            return f"{int(minut // 60)} soat oldin"
        return self.created.strftime('%H:%M | %d.%m.%Y')



class Subscription(models.Model):
    email = models.EmailField()
    is_trash = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"


class Contact(models.Model):
    user = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    is_trash = models.BooleanField(default=False)

    def response(self, contact_one=False):
        natija = {
            "id": self.id,
            "user": self.user,
            "phone": self.phone,
            "message": self.message,
            "is_trash": "is_trash" if self.is_trash else "is_trash emas!"
        }
        return natija

    def __str__(self):
        return f"{self.user} | {self.phone} | {self.message}"













