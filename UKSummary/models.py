from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

#EnergyHH countains all historical half hour data
class EnergyHH(models.Model):
    settleDate = models.DateField(_("Settlement Date"))
    settlePeriod = models.IntegerField(_("Settlement Period"))
    CCGT = models.IntegerField(_("Combined Gas Production"))
    oil = models.IntegerField(_("Oil Production"))
    coal = models.IntegerField(_("Coal Production"))
    nuclear = models.IntegerField(_("Nuclear Production"))
    wind = models.IntegerField(_("Wind Production"))
    pumped_storage = models.IntegerField(_("Pumped Storage Production"))
    hydro = models.IntegerField(_("Hydro Production"))
    OCGT = models.IntegerField(_("Open Cycle Gas Production"))
    other = models.IntegerField(_("Other Production"))
    france_IFA = models.IntegerField(_("France IFA Interconnector"))
    northern_ireland = models.IntegerField(_("Northern Ireland Interconnector"))
    netherlands = models.IntegerField(_("Netherlands Interconnector"))
    ireland = models.IntegerField(_("Ireland Interconnector"))
    biomass = models.IntegerField(_("Biomass Production"))
    belgium = models.IntegerField(_("Belgium Interconnector"))
    france_eleclink = models.IntegerField(_("France Eleclink Interconnector"))
    france_IFA2 = models.IntegerField(_("France IFA2 Interconnector"))
    norway = models.IntegerField(_("Norway Interconnector"))
