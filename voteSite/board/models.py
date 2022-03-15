from django.db import models


class Board(models.Model):
    category = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    recommend = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to="uploads")
    owner = models.ForeignKey('auth.user', related_name='boards', on_delete=models.CASCADE)
    vote = models.JSONField()

    class Meta:
        ordering = ['createdAt']
