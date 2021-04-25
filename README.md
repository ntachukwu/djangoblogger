# Django Blogger

This is a simple blog app where users can register and create an account so they can be able to make comments.<br />
**Link to Web App** [dennisthemenaceapp](www.dennisthemenaceapp.herokuapp.com) hosted on Heroku <br />
This documentation is to allow you to be able to deploy the app on Heroku 😊.<br />
Fork this repository so you can have your own copy. <br />
Head over to your Heroku dashboard. (if you don't have an account before you can just sign-up, it's free 😎)<br />
Link to [Heroku](www.heroku.com)
![screenshot](screenshots/1.png)
<br />
Create new App
![app creation screenshot](screenshots/3.png)
<br />
Enter the settings tab
![settings screenshot](screenshots/2.png)
<br />
From _Buildpacks_, click the _Add Buildpacks_ button. From the pop-up select _Python_.
![build screenshot](screenshots/4.png)
<br />
Next from _config vars_, click the _reveal vars_ button.
![config vars screenshot](screenshots/5.png)
<br />
Enter the value of SECRET\*KEY and DEBUG=False
![secret_key screenshot](screenshots/6.png)
<br />
Back at the tabs under the unique app name. Select the _Deploy_ tab, _Deployment Method_ GitHub
![deployment method](screenshots/7.png)
<br />
Enter your github log in details and connect to the appropriate repository you forked.
Next, _Manual deploy_ from the drop down select the branch of the repository you will like to deploy from.
![manaul deploy](screenshots/8.png)
<br />
With this your app will be deployed and build will commence.
<br />
**Congratulations your app is now live** 🤘🤘🤘
