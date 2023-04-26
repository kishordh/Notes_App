from django.db import models

# Create your models here.
class Efile(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.title
    