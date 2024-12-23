from django.db import models
from core.models import  AbstractModel
# Create your models here.
class Message(AbstractModel):
    name = models.CharField(
        max_length=120,
        default="",
        blank=True,
        verbose_name="Name",
        help_text="Enter your name",
    )
    email = models.EmailField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Email",
        help_text="Enter your email address",

    )
    subject = models.CharField(
        default="",
        max_length=120,
        blank=True,
        verbose_name="Subject",
        help_text="Enter your subject",
    )
    message = models.TextField(
        default="",
        blank=True,
        verbose_name="Message",
        help_text="Enter your message",
    )
    def __str__(self):
        return f'Message: {self.name}'
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['name']