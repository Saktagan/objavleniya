from django.db import models


class Rubric(models.Model):
    name = models.CharField(
        max_length=20, db_index=True, verbose_name="Nazvanie"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rubriki"
        verbose_name = "Rubrika"
        ordering = ["name"]


class Bb(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Name")
    content = models.TextField(
        null=True, blank=True, verbose_name="Description")
    price = models.FloatField(
        null=True, blank=True, verbose_name="Price")
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Published_date")

    rubric = models.ForeignKey(
        'Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubrika'
    )

    class Meta:
        verbose_name_plural = "Objavleniya"
        verbose_name = 'Objavlenie'
        ordering = ["-published"]