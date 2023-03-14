# django-UKSummary

## Overview
A django app that takes information from the BMRS API, stories it in a SQlite3 database and then displays a dashboard about UK Energy Generation. The dashboard provides a split of carbon producing vs zero carbon energy and a spit by power generation type.

![Page showing analysis of all time data](/assets/images/allTimePage.png)

![Page showing analysis of past year data](/assets/images/pastYearPage.png)

![Page showing analysis of past week data](/assets/images/pastWeekPage.png)

![Page showing analysis of today's data](/assets/images/todayPage.png)

Frontend uses boostrap and chart.js

## Quick Guide
1. Creat an .env file with the necessary variables as shown in .env.example
    - A django secret key can be generated in terminal by:
        - `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`. 
    - For the API_KEY that will be used to obtain information from BMRS,  an account can be created on [Elexon Portal](https://www.elexonportal.co.uk/registration/newuser?cachebust=dwtt3qfr9g).

2. Clone repo
    - `git clone https://github.com/https://github.com/Azamooos/EnergySummary.git`

3. Create a virtual environment, activate, and navigate into the correct folder (if required)
    - `python3 -m venv venv`
    - `venv/bin/activate`
    - `cd EnergySummary`

4. Install required packages by running:
    - `pip install -r requirements.txt`

5. Migrate the django project
    - `python manage.py migrate`

6. Open the server by running:
    - `python manage.py runserver`

7. The all time summary page can be found on 'http://127.0.0.1:8000/UKSummary/TotalSummary'.

## Planned future developments
- Include price data
- Include solar informatoin from [Sheffield Solar](https://www.solar.sheffield.ac.uk/pvlive/)
- Edit HMTL so site works on mobile
- Add section to the dashboard for analysis of imports/exports
- Use celery so database is updated regularly based on time not every refresh
- Make a version that uses postgreSQL so it's more appropriate for publishing


