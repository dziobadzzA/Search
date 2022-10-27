from django.db import models


# Create your models here.
class model(models.Model):
    vm = models.IntegerField()
    view = models.IntegerField()
    information = models.CharField(max_length=5)


class ship_name(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField()


class ship_class(models.Model):
    type_class = models.CharField(max_length=20)


class ship_type(models.Model):
    type_type = models.CharField(max_length=20)


class ship_place(models.Model):
    place = models.CharField(max_length=20)


class ship(models.Model):
    ship_class = models.ForeignKey(ship_class, on_delete=models.CASCADE)
    ship_name = models.ForeignKey(ship_name, on_delete=models.CASCADE)
    ship_type = models.ForeignKey(ship_type, on_delete=models.CASCADE)
    ship_place = models.ForeignKey(ship_place, on_delete=models.CASCADE)


class radio_device(models.Model):
    name_radio_device = models.CharField(max_length=20)


class param_radio_device(models.Model):
    param = models.CharField(max_length=20)


class table_radio(models.Model):
    radio_device = models.ForeignKey(radio_device, on_delete=models.CASCADE)
    param_radio_device = models.ForeignKey(param_radio_device, on_delete=models.CASCADE)
    param_value = models.FloatField()
    ship_name = models.ForeignKey(ship, on_delete=models.CASCADE)
