
**DATA EXTRACTION FROM API USING REQUESTS**

   In this project, RapidAPI was used to get data from a sport website. After which the data was stored into a dataframe and stored in XSLX and parquet. 

**AIM**
- To practice how to use the requests library.
- To learn how to extract data from website and put into a dataframe.
- Learn how to save files extracted from website.
- The use of env to hide API keys and gitignore to ignore the env file.

**REQUIREMENT**
- RapidAPI sign-in and subcription
- Installing and Importing of the below libraries:
   - requests
   - json
   - datetime
   - pyarrow
   - pandas
   - openpyxl
   - pyarrow
   - python-decouple

**PROCEDURE**
 - After subscribing to RAPIDAPI,
 - Install the required libraries: python-decouple,pyarrow,requests,openpxyl,datetime
 - Create an env file to store API key
 - Use of datetime and strip function to create different files when new information is retrieved from the website.
 - Save file in both XSLX and parquet formats.


 **Challenges/What I learnt**

Potential issues/challenges you might experience that I experienced:

 - I experienced some challenges especially using the RAPIDAPI as some of the the APIs failed initially.
 - I had difficulty in installing the dotenv library and eventually settled using the python-decouple.
 - Using the wrong format for datetime will return an error, so you have to use the strip functions to remove the spaces and also change the format from having : or .
 - I learnt working with APIs and using request library. Using JSON helped me when learning more about data extraction from json.