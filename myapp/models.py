from django.db import models





class Author(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=255)
    


class Post(models.Model):
    author =  models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    published_date = models.DateField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    text = models.CharField(max_length=155,null=True,blank=True)
    created_date = models.DateField(auto_now=True)