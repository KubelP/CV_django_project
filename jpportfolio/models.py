from django.db import models

class PortfolioCV(models.Model):
    body = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body


class Comments(models.Model):
    author = models.CharField(max_length=50)
    comment_body = models.CharField(max_length=500)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author

class Contact(models.Model):
    name = models.CharField(max_length=50)
    e_mail = models.EmailField()
    contact_body = models.TextField()

    def __str__(self) -> str:
        return self.name

class Portfolio(models.Model):
    proj_name = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)
    image = models.ImageField()
    project_body = models.CharField(max_length=1000)
    link = models.CharField(max_length=150)
    git_link = models.CharField(max_length=150, blank=True, null = True)

    def __str__(self) -> str:
        return self.proj_name

class MyContact(models.Model):
    name = models.CharField(max_length=100)
    my_image = models.ImageField()
    git_link = models.CharField(max_length=150)
    e_mail = models.EmailField()
    linked_link = models.CharField(max_length=150, blank=True, null = True)

    def __str__(self) -> str:
        return self.name

class CV(models.Model):
    name = models.CharField(max_length=100)
    profile = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    hobby = models.TextField()
    other = models.TextField()

    def __str__(self) -> str:
        return self.name