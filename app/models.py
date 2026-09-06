from django.utils import timezone

from django.db import models

"""
0: enregistré
1: envoyé
2: livré
"""
# Create your models here.
class Parcel(models.Model):
    tracking_number = models.CharField(max_length=11, unique=True)
    adress_dep = models.CharField(max_length=100)
    adress_arr = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
# Ceci est la foncion qui me permet de générer un numéro de suivi
    @classmethod
    def prochain_numero(cls):

        colis = cls.objects.filter(
            tracking_number__startswith="FR",
            tracking_number__endswith="HD"
         )
        dernier_numero = 0

        for colis_obj in colis:
            try:
                numero = int(colis_obj.tracking_number[2:6])

                if numero > dernier_numero:
                    dernier_numero = numero

            except (ValueError, TypeError):
                continue

        prochain = dernier_numero + 1

        if prochain > 9999:
            raise ValueError(
            "La limite de 9999 colis a été atteinte."
        )

        return f"FR{prochain:04d}HD"
# fin de la génération du numéro de suivi
#     
    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = self.prochain_numero()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Colis N°{self.id} - {self.weight}kg"

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    date_n = models.DateField(null=True, blank=True)