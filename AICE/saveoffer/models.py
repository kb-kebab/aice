from django.db import models

class SaveOfferView(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    
    class Meta:
        managed = True
        db_table = 'offer'