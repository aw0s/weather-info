# weather-info
Weather info collector app. This program collects weather data every particular time. It can also print current weather information of specific city. 

# Installation
1. Make sure that you've installed Python.
2. `Cd` into directory that you want the app to be installed in.  
3. Type `git clone https://github.com/aw0s/weather-info-collector.git`.  
4. Then `cd weather-info-collector`.  
6. Install requirements: `pip install -r requirements.txt`.  
7. Get API key from `https://home.openweathermap.org/api_keys`.  
8. Create `.env` file by typing `touch src/.env` and put `API_KEY=(your API key)` there.
10. After that, you should be able to run the program.  
11. Type `python src/main.py`.  And that's all. It should work :D  

 # Documentation
 By running `weather-info-collector` without any parameters, the application will only collect data. By passing arguments specified below to the program, you can enter specific mode.
 
 ## Arguments
 ### weather-info
 This command is responsible for printing weather information of the particular city.
 
 ### db-read-mode
 Using this command, you can get record from database by id.
 
 ## Settings
 `DB_PATH` - Database path.  
 `CITY` - Records of this city will be stored in the database.  
 `SAVE_RECORD_TIME` - Time interval between which records will be written to the database. 
