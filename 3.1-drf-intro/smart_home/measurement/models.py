from django.db import models
# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

# датчик:
class Sensor(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100, blank=True)


# измерение температуры:
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)





