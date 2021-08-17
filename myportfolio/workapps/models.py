from django.db import models

#Home section

class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting_1 = models.CharField(max_length=5)
    greeting_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    #save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# About section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About, 
                                    on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


#skills section

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    Category = models.ForeignKey(Category,
                                    on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)



# portfolio section
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio{self.id}'


































#     short_description =models.TextField()
#     description = models.TextField()
#     image = models.ImageField(upload_to="about")

#     class Meta:
#         verbose_name = "About me"
#         verbose_name_plural = "About me"

#     def __str__(self):
#         return "About me"

# #Service Model
# class Service(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Service name")
#     description = models.TextField(verbose_name="About services")

#     def __str__(self):
#         return self.name

# #Recent Work model
# class RecentWork(models.Model):
#     title = models.CharField(max_length=100, verbose_name="work title")
#     image = models.ImageField(upload_to="works")

#     def __str__(self):
#         return self.title

# #clients model
# class Client(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Client name")
#     description = models.TextField(verbose_name="Client say")
#     image = models.ImageField(upload_to="clients", default ="default.png")

#     def __str__(self):
#         return self.name
