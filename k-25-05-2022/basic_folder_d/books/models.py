from django.db import models
from django.template.defaultfilters import slugify


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    pages = models.IntegerField()
    slug = models.SlugField(null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
        )