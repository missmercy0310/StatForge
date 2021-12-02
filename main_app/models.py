from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class RPG(models.Model):
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    stats_name = models.CharField(max_length=500, default="Stats")
    classes_name = models.CharField(max_length=500, default="Classes")
    entities_name = models.CharField(max_length=500, default="Playable Entities")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Stat(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    max_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rpg = models.ForeignKey(RPG, on_delete=models.CASCADE, related_name="stats")

    def __str__(self):
        return f"{self.rpg.title}, {self.title}"

    class Meta:
        ordering = ['title']

class Classification(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    rpg = models.ForeignKey(RPG, on_delete=models.CASCADE, related_name="classes")

    def __str__(self):
        return f"{self.rpg.title}, {self.title}"

    class Meta:
        ordering = ['title']

class Entity(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    class_options = models.ManyToManyField(Classification, through='ClassOption')
    stat_buffs = models.ManyToManyField(Stat, through='StatBuff')
    created_at = models.DateTimeField(auto_now_add=True)
    rpg = models.ForeignKey(RPG, on_delete=models.CASCADE, related_name="entities")

    def __str__(self):
        return f"{self.rpg.title}, {self.title}"

    class Meta:
        ordering = ['title']

class ClassOption(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.entity.rpg.title}, {self.entity.title}, {self.classification.title}"

class StatBuff(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
    buff = models.IntegerField()

    def __str__(self):
        return f"{self.entity.rpg.title}, {self.entity.title}, {self.stat.title}"