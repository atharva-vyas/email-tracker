# Email-Tracker
**A simple email tracker, primarily made using nodeJS**
****
**Features:-**
1) Get the exact time the email was opened
2) Get GeoLocation of the Recipient
3) Get additional Info such ISP, ASN, etc.
****
**index.js:-** helps generate trackingID's, keeps track of trackingID's, keeps track of how many times a email is read

**main.py:-** helps communicate with index.js and fetch data<br/><br/>


**How to configure**
1) Get your mongoDB cluster url
2) Add your mongoDB cluster url to a .env file
3) Deploy the index.js app using Heroku, AWS, etc.
4) change the url variable in main.py with the url of your deployed application

**How to Track your emails**
1) create a mail tracking id, using main.py
2) manually embed the tracking id as a image with your email
