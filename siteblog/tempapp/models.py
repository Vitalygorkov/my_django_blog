from django.db import models

class Temp(models.Model):
    temp_date = models.DateTimeField(auto_now_add = True, blank = True)
    value = models.IntegerField(default=0)
    self_name = str(temp_date)

    def __str__(self):
        return self.self_name
