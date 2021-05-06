from Monster_Hunter.models.Hunter import Hunter
from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Object import Object
from Monster_Hunter.models.Palico import Palico
from django.db import models


class Palico_lent(models.Model):
    delivery_date = models.DateTimeField()
    palico_id = models.ForeignKey(Palico, on_delete=models.CASCADE)
    hunter_lent = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    return_date = models.DateTimeField()

    def __str__(self):
        return "Lend "+ self.palico_id.name + " to " + self.hunter_lent.name

    class Meta:
        unique_together = [["delivery_date","palico_id"],["delivery_date","hunter_lended"]]


class Inventory(models.Model):
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['hunter_id']
        unique_together = [["hunter_id", "object_id"]]


class Recipes(models.Model):
    name = models.CharField(max_length=50)
    object_id1 = models.ForeignKey(Object, on_delete=models.CASCADE)
    object_id_2 = models.ForeignKey(Object, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['object_id1']
        # unique_together = [["object_id1", "object_id2"]]


class Reward_object(models.Model):
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE)
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['monster_id']
        unique_together = [["object_id", "hunter_id"],["monster_id", "hunter_id"]]
