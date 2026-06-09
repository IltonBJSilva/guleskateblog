from django.db import models


class Mod(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True
    )

    short_description = models.CharField(
        max_length=255
    )

    description = models.TextField()

    minecraft_version = models.CharField(
        max_length=50
    )

    image = models.ImageField(
        upload_to="mods/images/"
    )

    github_url = models.URLField(
        blank=True
    )

    download_url = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title