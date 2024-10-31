from django.db import models

# Create your models here.
class EventPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True)
    event_date = models.DateField()
    event_coordinator = models.CharField(max_length=100)

    def _str_(self):
        return self.title