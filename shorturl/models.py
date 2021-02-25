from django.db import models

# Create your models here.
class Mainurl(models.Model):
    encoded = models.CharField(max_length = 200)
    original_url = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.encoded