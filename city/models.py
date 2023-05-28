from django.db import models


class State(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=2)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    state = models.ForeignKey(State, related_name='cities', on_delete=models.CASCADE)
    population = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Cities'

    def __str__(self) -> str:
        return self.name
