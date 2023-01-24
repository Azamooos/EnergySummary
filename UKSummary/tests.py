from django.test import TestCase
import datetime
from datetime import date
from .models import EnergyHH
from .utils import updateHistoric

class EnergyHHModelTests(TestCase):

    def test_invalid_api_request(self):
        """
        when an invalid api request is passed, code ignores and carries on using current database without update
        """
        
        #Create a database where the last date is in the future which should make invalid url for BMRS API
        futureDate = date(2070,1,1)
        EnergyHH.objects.create(settleDate = futureDate, settlePeriod = 1, 
        CCGT = 2, oil = 3, coal = 4, nuclear = 5, wind = 6, 
        pumped_storage = 7, hydro = 8,OCGT = 9, other = 10, 
        france_IFA = 11, northern_ireland = 12, netherlands = 13, 
        ireland = 14, biomass = 15, belgium = 16, france_eleclink = 17, 
        france_IFA2 = 18, norway = 19)

        #Run update historic
        updateInfo = updateHistoric()

        #Should give false for updated database and the initial date for past updated date
        self.assertIs(updateInfo['updatedBool'], False)
        self.assertEqual(updateInfo['lastUpdated'], futureDate)
    

    def test_valid_api_request(self):
        """
        when a valid api request is passed, database is updated
        """
        pastDate = date.today() - datetime.timedelta(days = 2)
        #Create a database where the last date is two days in the past making valid BMRS API request
        EnergyHH.objects.create(settleDate = pastDate, settlePeriod = 1, 
        CCGT = 2, oil = 3, coal = 4, nuclear = 5, wind = 6, 
        pumped_storage = 7, hydro = 8,OCGT = 9, other = 10, 
        france_IFA = 11, northern_ireland = 12, netherlands = 13, 
        ireland = 14, biomass = 15, belgium = 16, france_eleclink = 17, 
        france_IFA2 = 18, norway = 19)

        #Run update historic
        updateInfo = updateHistoric()

        #Should give true for updated database and today for the last updated date
        self.assertIs(updateInfo['updatedBool'], True)    
        self.assertEqual(updateInfo['lastUpdated'], date.today())