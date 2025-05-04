from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(editable = True, default=datetime.now)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, unique=True)  # Unique token

    def __str__(self):
        return self.email

class ContactQuery(models.Model):
    name = models.CharField(max_length=255)  # Store user's name
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_on = models.DateTimeField(editable = True, default=datetime.now)

    def __str__(self):
        return f"Query from {self.name} ({self.email})"
