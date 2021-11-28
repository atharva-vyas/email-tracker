# Email-Tracker
**A simple email tracker, primarily made using nodeJS**
****
**index.js:-** helps generate trackingID's, keeps track of trackingID's, keeps track of how many times the mail was read

**main.py:-** helps communicate with index.js and fetch data


**How to configure**
1) Get your mongoDB cluster url
2) Add your mongoDB cluster url to a .env file
3) Deploy the index.js app using Heroku, AWS, etc.
4) change the url variable in main.py with the url of your deployed application

**How to Track your emails**
1) create a mail tracking id, using main.py
2) embed the tracking id as a image with your email (dont worry the recipient will not be able to see it).
3) wait for him to open your mail
