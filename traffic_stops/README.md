# Illinois traffic stops
## A data journalism practice rig
Since 2004, Illinois has required police officers to record data on traffic stops, including the race of the driver, the reason for the stop and the outcome, among other data points.  

Twenty years later, journalists with WBEZ and the Investigative Project on Race and Equity compiled this database of every traffic stop reported to the state during that time, publishing a series of stories along with training materials to demonstrate how to use this information.  

This repository includes a version of the complete 46 million-row database, updated through 2024, along with documentation to help you understand how to investigate further. Along the way, you’ll learn practical components of data journalism, including sorting/filtering, grouping, joining, measuring change over time.  

## Getting started

Clone the repository:   
[https://github.com/mattkiefer/data-journalism](https://github.com/mattkiefer/data-journalism)

Download the database:   
[https://drive.google.com/file/d/1qlsd7pveQodROyiI9kK4QfqATTliYhTH/view?usp=drive\_link](https://drive.google.com/file/d/1qlsd7pveQodROyiI9kK4QfqATTliYhTH/view?usp=drive_link)

Extract/unzip the database in your local repo, i.e. this path:   
`\~/Documents/GitHub/data-journalism/traffic\_stops`

Use a virtualenv (from terminal):  
```
cd ~/Documents/GitHub/data-journalism/traffic_stops  
python3 -m venv .venv  
. .venv/bin/activate  
pip install -r requirements.txt
```

## Using the database

You can use SQL, python/pandas or R to work with the database.

The file [console.py](http://console.py) includes sample queries and analysis code to get started in python.

To access the sample objects in [console.py](http://console.py), start a python shell in your terminal:  
```
ipython  
from console import *
```

## Exercises

### basic querying

* Modify the SQL query to select various slices of data 	  
  * Refer to stops table  
* Filter and sort data   
  * Use SQL, python or R  
* Group data by race, year and/or agency  
  * Group by multiple fields, e.g. agency and year

### analysis

* Find percentages of total stops by racial groups  
  * Divide group totals by overall total  
* Compare traffic stop percentages against local population demographics   
  * Refer to the agencies table  
* Assess changes over time  
  * Analyze data by year

### Fact-checking

* Verify numbers from stories by WBEZ et al   
  * See recommended reading below for links  
* Verify numbers found in IDOT PDF reports  
  * See recommended reading below for links  
* Verify numbers from college traffic stops story   
  * From database, load agency.student\_demos as JSON

### Updates

* Update findings from published stories   
  * use 2024 numbers, which were just released this summer  
* Determine if racial disparities are increasing, decreasing or staying the same in:  
  * Chicago  
  * Evergreen Park  
  * Northern Illinois University  
  * Illinois statewide

## Recommended reading

* [Illinois traffic stops of Black drivers reach record highs \- WBEZ Chicago](https://www.wbez.org/wbez-investigations/2023/09/27/illinois-traffic-stops-of-black-drivers-hit-20-year-high)  
* [Black drivers in Illinois are pulled over by police more, mostly for non-moving violations \- Chicago Sun-Times](https://chicago.suntimes.com/2023/9/29/23894092/black-drivers-are-pulled-over-by-police-its-mostly-for-non-moving-violations)  
* [What we learned by analyzing 42 million Illinois traffic stop records](https://www.raceandequityproject.org/blog/what-we-learned-by-analyzing-42-million-illinois-traffic-stop-records)  
* [Ticketed, Towed, and Traumatized: Driving While Black on Campus \- Capital B News](https://capitalbnews.org/illinois-college-police-black-drivers/)  
* [Evergreen Park stops more Black drivers than almost anywhere else in Illinois](https://www.wbez.org/2023/12/20/black-drivers-accuse-evergreen-park-of-racial-profiling)  
* [Oak Park police stop more Black individuals than white, data shows \- Wednesday Journal](https://www.oakpark.com/2024/03/27/oak-park-police-traffic-stops-data/)  
* [Dexter Reed shooting sparks outcry about traffic stops \- WBEZ Chicago](https://www.wbez.org/criminal-justice/2024/04/12/dexter-reed-shooting-sparks-outcry-about-traffic-stops)  
* [Look up your local Illinois police traffic stop data](https://interactive.wbez.org/traffic-stops/illinois-statewide/)  
* [Traffic stops database technical documentation](https://docs.google.com/document/d/1Yk1J9SAPfZXfYk2Kb-z6K4p4eU6Rhnoc0RciRscymgY/edit?tab=t.0#heading=h.3f2v1umji09d)  
* [Illinois Department of Transportation Traffic Stop Study](https://idot.illinois.gov/transportation-system/local-transportation-partners/law-enforcement/reporting/illinois-traffic-and-pedestrian-stop-study.html)  
  * [PDF reports](https://idot.illinois.gov/transportation-system/local-transportation-partners/law-enforcement/reporting/illinois-traffic-and-pedestrian-stop-study/studies.html)

