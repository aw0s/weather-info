# weather-info
Weather info collector app. This program collects weather data every particular time. It can also print current weather information from specific city. 

# Installation
Make sure that you've installed Python. `Cd` into directory that you want the app to be installed in. Type `git clone https://github.com/aw0s/weather-info-collector.git`. Then `cd weather-info-collector`. Install requirements: `pip install -r requirements.txt`. After that, you should be able to run the program.
Type `python src/main.py`. And that's all. It should work :D 

 # Documentation
 If you run the app, you should see the command prompt.
 
 ## Commands
 ### weather-info
 This command is responsible for printing weather information of the particular city.
 
 ### db-read-mode
 Using this command, you can get record from database by id.
 
 ## Settings
 `DB_PATH` - Database path. 
 `CITY` - Records of this city will be stored in the database. 
 `SAVE_RECORD_TIME` - Time interval between which records will be written to the database.
