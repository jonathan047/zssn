from django.db.models import TextChoices


class ChoicesCategoriaComercio(TextChoices):
    TROCAR_MED = "TMED", "Trocar por medicação"
    TROCAR_MUNICAO ="TM", "Trocar munição"
    TROCAR_AGUA = "TA", "Trocar por água" 
    TROCAR_ALIMENTO = "TAL","Trocar por alimento"