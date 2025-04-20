from django.db import models

class Fund(models.Model):
    class FundStructureChoice(models.TextChoices):
        OPEN = "OPEN", "Abierto"
        CLOSE = "CLOSE", "Cerrado"

    class InstitutionChoice(models.TextChoices):
        BHD = "BHD", "bhd"
        PPL = "PPL", "popular"

    class CurrencyChoice(models.TextChoices):
        DOP = "DOP", "dop"
        USD = "USD", "usd"
        EUR = "EUR", "eur"
        
    name = models.CharField(max_length=250, verbose_name="Nombre del fondo")
    structure = models.CharField(max_length=5, choices=FundStructureChoice, default=FundStructureChoice.CLOSE, verbose_name="Estructura del fondo")
    institution = models.CharField(max_length=255, verbose_name="Nombre de la institucion", choices=InstitutionChoice, default=InstitutionChoice.BHD)
    register_number = models.CharField(max_length=255, blank=True, default="", verbose_name="Numero de registro")
    launch = models.DateField(max_length=255, blank=True, default="", verbose_name="Fecha de constitucion")
    administrator = models.CharField(max_length=255, blank=True, default="", verbose_name="Administrador del fondo")
    administration_fee = models.DecimalField( decimal_places=6, max_digits=13, blank=True, default=None, verbose_name="Comision por administracion")
    performance_fee = models.DecimalField( decimal_places=6, max_digits=13, blank=True, default=None, verbose_name="Comision por desempeno")
    early_redemption_fee = models.DecimalField( decimal_places=6, max_digits=13, blank=True, default=None, verbose_name="Comision por rescate anticipado")
    currency = models.CharField(choices=CurrencyChoice, default=CurrencyChoice.DOP, verbose_name="Moneda de Inversion")
    minimum_initial_investment = models.DecimalField( decimal_places=2, max_digits=13, blank=True, default=None, verbose_name="Inversion Inicial Minima")
    minimum_addition = models.DecimalField( decimal_places=2, max_digits=13, blank=True, default=None, verbose_name="Inversion minima de adiciones")
    minimum_balance = models.DecimalField( decimal_places=2, max_digits=13, blank=True, default=None, verbose_name="Saldo minimo de permanencia")
    

    def __str__(self):
        return self.name
    
class FundUpdate(models.Model):
    name = models.ForeignKey(Fund,on_delete=models.CASCADE, default=1)
    current_share_value = models.DecimalField(decimal_places=8, max_digits=13, blank=True, default=None, verbose_name="Valor de la cuota del dia")
    previous_share_value = models.DecimalField(decimal_places=8, max_digits=13, blank=True, default=None, verbose_name="Valor de la cuota del dia anterior")
    fund_value = models.DecimalField(decimal_places=2, max_digits=13, blank=True, default=None, verbose_name="Valor del fondo")
    number_of_contributors = models.IntegerField(blank=True, default=None, verbose_name="Number de aportantes")
    return_last_30_days = models.DecimalField(decimal_places=8, max_digits=13, blank=True, default=None, verbose_name="Rentabilidad de ultimos 30 dias")
    return_last_90_days = models.DecimalField(decimal_places=8, max_digits=13, blank=True, default=None, verbose_name="Rentabilidad de ultimos 90 dias")
    return_last_180_days = models.DecimalField(decimal_places=8, max_digits=13, blank=True, default=None, verbose_name="Rentabilidad de ultimos 180 dias")
    return_last_365_days = models.DecimalField(decimal_places=8, max_digits=13, blank=True, default=None, verbose_name="Rentabilidad de ultimos 365 dias")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return str(self.name)