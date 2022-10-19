from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"Language: {self.language}"

class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return f"Tag: {self.tag}"

class Snip(models.Model):
    title = models.CharField(max_length=300, unique=True)
    snippet = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    pinned = models.BooleanField(default=False)
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Snip: {self.title}"