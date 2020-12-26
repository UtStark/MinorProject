from django.db import models

class Attendance(models.Model):
    enum = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    attendance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Attendance'

    def __str__(self):
        return self.name + "- "+ str(self.enum)

