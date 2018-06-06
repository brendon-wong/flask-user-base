In order to have Heroku recognize the instance folder, it must be committed to version control due to Heroku's [ephemeral filesystem](https://simpleit.rocks/avoid-using-flask-instance-folder-when-deploying-to-heroku/).

Typically, this folder should not be committed to version control and should be independently uploaded to the server instead. It may be acceptable to commit the instance folder to version control if the repository will never be shared publicly and is only accessible to trusted collaborators, or if it does not contain any data that should be kept private.