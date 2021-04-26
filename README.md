# Django Blogger

This is a simple blog app where users can register and create an account so they can be able to make comments.\
**Link to Web App** [dennisthemenaceapp](https://dennisthemenaceapp.herokuapp.com/) hosted on Heroku\

This documentation is to allow you to be able to deploy the app on Heroku 😊.\
Fork this repository so you can have your own copy.\
Head over to your Heroku dashboard. (if you don't have an account before you can just sign-up, it's free 😎)\
Link to [Heroku](https://www.heroku.com)
![screenshot](screenshots/1.png)
\
Create new App
![app creation screenshot](screenshots/3.png)
\
Enter the settings tab
![settings screenshot](screenshots/2.png)
\
From _Buildpacks_, click the _Add Buildpacks_ button. From the pop-up select _Python_.
![build screenshot](screenshots/4.png)
\
Next from _config vars_, click the _reveal vars_ button.
![config vars screenshot](screenshots/5.png)
\
Enter the value of SECRET*KEY and DEBUG=False
![secret_key screenshot](screenshots/6.png)
\
Back at the tabs under the unique app name. Select the \_Deploy* tab, _Deployment Method_ GitHub
![deployment method](screenshots/7.png)
\
Enter your github log in details and connect to the appropriate repository you forked.
Next, _Manual deploy_ from the drop down select the branch of the repository you will like to deploy from.
![manaul deploy](screenshots/8.png)
\
With this your app will be deployed and build will commence.
\
**Congratulations your app is now live** 🤘🤘🤘
