from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    #self.pk = 해당 포스트의 pk값 self.title = 해당 포스트의 title값

# Create your models here.
