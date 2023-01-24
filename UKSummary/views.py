from django.shortcuts import render
from django.http import HttpResponse
from .utils import updateHistoric
from .utils import findCarbonSplit
from .models import EnergyHH
from django.db.models import Avg
from django.db.models import Max
from dateutil.relativedelta import relativedelta  
import calendar
import datetime

def totalSummary(request):
    #Updates database to current date
    updateInfo = updateHistoric()
    print(updateInfo)
    '''
    Creates inputs for doughnut charts
    '''
    #Creates labels for carbon split doughnut chart
    carbonDoughnutLabels = ['Fossil Fuels (GW)', 'Low Carbon (GW)']
    
    #Creates labels for energy split doughnut chart
    energyDougnutLabels = ['Gas (GW)', 'Coal (GW)', 'Wind (GW)', 'Nuclear (GW)', 'Biomass (GW)']

    #Finds data from utils function
    carbonDoughnutData, energyDoughnutData = findCarbonSplit(EnergyHH.objects.all())
    '''
    Creates inputs for carbon split line chart
    '''

    #Creates empty lists for data to be passed through to chart
    timeLineLabel = []
    carbonYesLineData = []
    carbonNoLineData = []
    gasLineData = []
    coalLineData = []
    windLineData = []
    nuclearLineData = []
    hydroLineData = []
    biomassLineData = []

    #Finds earliest and latest year
    objEarly = EnergyHH.objects.earliest('settleDate')
    objLate = EnergyHH.objects.latest('settleDate')
    fieldObject = EnergyHH._meta.get_field('settleDate')
    earliestDate = fieldObject.value_from_object(objEarly)
    latestDate = fieldObject.value_from_object(objLate)

    #Iterates through the years populating chart lists
    for i in range(earliestDate.year,(latestDate.year + 1)):
        #Records which year the data is from
        timeLineLabel.append(str(i))

        #Queries for that year
        yearQuery = EnergyHH.objects.filter(settleDate__year = i)

        #Finds carbon and energy data splits
        carbonSplits, energySplits = findCarbonSplit(yearQuery)

        #Populates line data for that year
        carbonYesLineData.append(carbonSplits[0])
        carbonNoLineData.append(carbonSplits[1])
        gasLineData.append(energySplits[0]) 
        coalLineData.append(energySplits[1]) 
        windLineData.append(energySplits[2]) 
        nuclearLineData.append(energySplits[3]) 
        biomassLineData.append(energySplits[4]) 


    #Renders and passes data to html
    return render(request, 'UKSummary/totalSummary.html', {
        'carbonDoughLabels' : carbonDoughnutLabels,
        'carbonDoughData' : carbonDoughnutData,
        'energyDoughLabels' : energyDougnutLabels,
        'energyDoughData' : energyDoughnutData,
        'timeLineLabel' : timeLineLabel,
        'carbonYesLineData' : carbonYesLineData,
        'carbonNoLineData' : carbonNoLineData,
        'gasLineData' : gasLineData,
        'coalLineData' : coalLineData,
        'windLineData' : windLineData,
        'nuclearLineData' : nuclearLineData,
        'biomassLineData' : biomassLineData
    })

def yearlySummary(request):
    #Updates database to current date
    updateInfo = updateHistoric()
    print(updateInfo)
    '''
    Creates inputs for doughnut charts
    '''
    #Creates labels for carbon split doughnut chart
    carbonDoughnutLabels = ['Fossil Fuels (GW)', 'Low Carbon (GW)']
    
    #Creates labels for energy split doughnut chart
    energyDougnutLabels = ['Gas (GW)', 'Coal (GW)', 'Wind (GW)', 'Nuclear (GW)', 'Biomass (GW)']

    #Finds latest date in database
    objLate = EnergyHH.objects.latest('settleDate')
    fieldObject = EnergyHH._meta.get_field('settleDate')
    latestDate = fieldObject.value_from_object(objLate)
    prevYearDate = latestDate - relativedelta(years=1)  

    #Finds data from utils function for last year
    carbonDoughnutData, energyDoughnutData = findCarbonSplit(EnergyHH.objects.filter(settleDate__range = (prevYearDate, latestDate)))
    
    '''
    Creates inputs for carbon split line chart
    '''

    #Creates empty lists for data to be passed through to chart
    timeLineLabel = []
    carbonYesLineData = []
    carbonNoLineData = []
    gasLineData = []
    coalLineData = []
    windLineData = []
    nuclearLineData = []
    hydroLineData = []
    biomassLineData = []



    #Iterates through the the months in the last year populating chart lists
    for i in range(12):

        iterDate = prevYearDate + relativedelta(months=i+1)
        #Records which month the data is from
        timeLineLabel.append(iterDate.strftime("%d/%m/%Y"))

        #Queries for that month range
        monthQuery = EnergyHH.objects.filter(settleDate__range = ((iterDate - relativedelta(months=1)), iterDate))

        #Finds carbon and energy data splits
        carbonSplits, energySplits = findCarbonSplit(monthQuery)

        #Populates line data for that month
        carbonYesLineData.append(carbonSplits[0])
        carbonNoLineData.append(carbonSplits[1])
        gasLineData.append(energySplits[0]) 
        coalLineData.append(energySplits[1]) 
        windLineData.append(energySplits[2]) 
        nuclearLineData.append(energySplits[3]) 
        biomassLineData.append(energySplits[4]) 


    #Renders and passes data to html
    return render(request, 'UKSummary/yearlySummary.html', {
        'carbonDoughLabels' : carbonDoughnutLabels,
        'carbonDoughData' : carbonDoughnutData,
        'energyDoughLabels' : energyDougnutLabels,
        'energyDoughData' : energyDoughnutData,
        'timeLineLabel' : timeLineLabel,
        'carbonYesLineData' : carbonYesLineData,
        'carbonNoLineData' : carbonNoLineData,
        'gasLineData' : gasLineData,
        'coalLineData' : coalLineData,
        'windLineData' : windLineData,
        'nuclearLineData' : nuclearLineData,
        'biomassLineData' : biomassLineData
    })

def weeklySummary(request):
    #Updates database to current date
    updateInfo = updateHistoric()
    print(updateInfo)
    '''
    Creates inputs for doughnut charts
    '''
    #Creates labels for carbon split doughnut chart
    carbonDoughnutLabels = ['Fossil Fuels (GW)', 'Low Carbon (GW)']
    
    #Creates labels for energy split doughnut chart
    energyDougnutLabels = ['Gas (GW)', 'Coal (GW)', 'Wind (GW)', 'Nuclear (GW)', 'Biomass (GW)']

    #Finds latest date in database
    objLate = EnergyHH.objects.latest('settleDate')
    fieldObject = EnergyHH._meta.get_field('settleDate')
    latestDate = fieldObject.value_from_object(objLate)
    prevWeekDate = latestDate - relativedelta(days=7)  

    #Finds data from utils function for last year
    carbonDoughnutData, energyDoughnutData = findCarbonSplit(EnergyHH.objects.filter(settleDate__range = (prevWeekDate, latestDate)))
    
    '''
    Creates inputs for carbon split line chart
    '''

    #Creates empty lists for data to be passed through to chart
    timeLineLabel = []
    carbonYesLineData = []
    carbonNoLineData = []
    gasLineData = []
    coalLineData = []
    windLineData = []
    nuclearLineData = []
    hydroLineData = []
    biomassLineData = []



    #Iterates through the the months in the last year populating chart lists
    for i in range(7):

        iterDate = prevWeekDate + relativedelta(days=i+1)
        #Records which month the data is from
        timeLineLabel.append(calendar.day_name[iterDate.weekday()])

        #Queries for that month range
        dayQuery = EnergyHH.objects.filter(settleDate__range = ((iterDate - relativedelta(days=1)), iterDate))

        #Finds carbon and energy data splits
        carbonSplits, energySplits = findCarbonSplit(dayQuery)

        #Populates line data for that month
        carbonYesLineData.append(carbonSplits[0])
        carbonNoLineData.append(carbonSplits[1])
        gasLineData.append(energySplits[0]) 
        coalLineData.append(energySplits[1]) 
        windLineData.append(energySplits[2]) 
        nuclearLineData.append(energySplits[3]) 
        biomassLineData.append(energySplits[4]) 


    #Renders and passes data to html
    return render(request, 'UKSummary/weeklySummary.html', {
        'carbonDoughLabels' : carbonDoughnutLabels,
        'carbonDoughData' : carbonDoughnutData,
        'energyDoughLabels' : energyDougnutLabels,
        'energyDoughData' : energyDoughnutData,
        'timeLineLabel' : timeLineLabel,
        'carbonYesLineData' : carbonYesLineData,
        'carbonNoLineData' : carbonNoLineData,
        'gasLineData' : gasLineData,
        'coalLineData' : coalLineData,
        'windLineData' : windLineData,
        'nuclearLineData' : nuclearLineData,
        'biomassLineData' : biomassLineData
    })

def liveSummary(request):
    #Updates database to current date
    updateInfo = updateHistoric()
    print(updateInfo)
    '''
    Creates inputs for doughnut charts
    '''
    #Creates labels for carbon split doughnut chart
    carbonDoughnutLabels = ['Fossil Fuels (GW)', 'Low Carbon (GW)']
    
    #Creates labels for energy split doughnut chart
    energyDougnutLabels = ['Gas (GW)', 'Coal (GW)', 'Wind (GW)', 'Nuclear (GW)', 'Biomass (GW)']

    #Finds latest date in database
    objLate = EnergyHH.objects.latest('settleDate')
    fieldObject = EnergyHH._meta.get_field('settleDate')
    latestDate = fieldObject.value_from_object(objLate)

    todayQuery = EnergyHH.objects.filter(settleDate = latestDate)
    #Finds data from utils function for last year
    carbonDoughnutData, energyDoughnutData = findCarbonSplit(todayQuery)
    
    '''
    Creates inputs for carbon split line chart
    '''

    #Creates empty lists for data to be passed through to chart
    timeLineLabel = []
    carbonYesLineData = []
    carbonNoLineData = []
    gasLineData = []
    coalLineData = []
    windLineData = []
    nuclearLineData = []
    hydroLineData = []
    biomassLineData = []

    #Finds maximum period for today
    latestPeriod = todayQuery.aggregate(Max('settlePeriod'))
    recentPeriod = latestPeriod.get('settlePeriod__max')

    #Converts date to datetime starting at midnight
    latestDateTime = datetime.datetime.combine(latestDate, datetime.datetime.min.time())

    #Iterates through all periods in latest date
    for i in range(recentPeriod):
        i += 1
        #Adds 30 minutes for each period iterated through
        iterTime = latestDateTime + datetime.timedelta(minutes = i*30)

        #Records which time the data is from
        timeLineLabel.append(iterTime.strftime("%H:%M"))

        #Queries for that period
        periodQuery = todayQuery.filter(settlePeriod = i)

        #Finds carbon and energy data splits
        carbonSplits, energySplits = findCarbonSplit(periodQuery)

        #Populates line data for that month
        carbonYesLineData.append(carbonSplits[0])
        carbonNoLineData.append(carbonSplits[1])
        gasLineData.append(energySplits[0]) 
        coalLineData.append(energySplits[1]) 
        windLineData.append(energySplits[2]) 
        nuclearLineData.append(energySplits[3]) 
        biomassLineData.append(energySplits[4]) 


    #Renders and passes data to html
    return render(request, 'UKSummary/liveSummary.html', {
        'carbonDoughLabels' : carbonDoughnutLabels,
        'carbonDoughData' : carbonDoughnutData,
        'energyDoughLabels' : energyDougnutLabels,
        'energyDoughData' : energyDoughnutData,
        'timeLineLabel' : timeLineLabel,
        'carbonYesLineData' : carbonYesLineData,
        'carbonNoLineData' : carbonNoLineData,
        'gasLineData' : gasLineData,
        'coalLineData' : coalLineData,
        'windLineData' : windLineData,
        'nuclearLineData' : nuclearLineData,
        'biomassLineData' : biomassLineData
    })