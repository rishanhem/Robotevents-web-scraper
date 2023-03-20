# RobotEvents web-scraper

Functionality - 
Reads the team number from the RobotEvents teams list of an event and appends their world skills rank to a new .csv file.
Basically, ranks the teams at an event by World skills rank.


FIRST how to get the teams list - 
1. Go to the event on robotevents
2. Click on teams and scroll all the way down
3. Click on the teams button 
4. Upload it into Google Drive
5. Open the file and download as a .csv file



---How to Work---
1. Download the .zip file 
2. replace vrc.csv with the team .csv file that was renamed to vrc.csv
3. Run the program 

If running more than once, replace vrc1.csv with a blank version after every time


•Utilized Python’s Requests and CSV libraries to read data from a CSV file and use that with the Requests library to get HTML from a website
•Scraped data from the website and wrote into another CSV file with all the data from the previous CSV and the web scraped data combined
