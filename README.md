# Movie Website using Django and deployed in Heroku
## Introduction
This website is built with Django which is a python framework for web development.
You can check out this website clicking here, https://centmovies.herokuapp.com
This website has basic features of like, dislike and adding reviews to hundreds of movies listed there. The movies listed in this website can be grouped by director name, cast name, language and by year of release. 
The movies can also be ordered by the available genre. The data used for this website is got from IMDB official website.
## Files in the project
- **/movie/views.py**: This is the app file that contains the logic of all the view functions in the backend which generate dynamic contents to HTML template.
- **/movie/models.py**: Contains Django models used for storing movie data.
- **/movie/forms.py**: python app file  required for creatingform in this appliation.
- **/movie/urls.py**: python app file  required for url mapping to all the view functions.
- **/movie/admin.py**: python app file  required for registering to django-administration of this appliation.
- **/movie/tests.py**: python app file  required for testing of this appliation.
- **/movie/apps.py**: python app file  required for registering the movie app to django movie_site project of this appliation.
- **/movie_site/**: python main project folder in which movie app is created.
- **Procfile**: file required for deployment i heroku.
- **requirements.txt**: list of Python packages installed (also required for Heroku)
- **movie/templates/**: folder with all HTML files
- **movie/static/**: for all JS scripts and CSS files
## Usage
### Clone/Modify app
1. Modify movie folder or create a new app in the main movie_site project folder.

    For modifying existance code or creating new app, These lines need to be edited in movie_site/settings.py are shown below:
```python
SECRET_KEY ='<your secret key>'
ALLOWED_HOSTS = ['<your allowed host>']
DATABASES = {<your database settings>}
```
2. Run makemigrations and migrate command from the terminal to create the table with the link to your database.

3. Run createsuperuser command to register to django admin panel.

4. Create new app in movie_site project folder using following command,
    
```console
C:\<path to movie_site>\python manage.py startapp <your app name>
```
## Areas of improvement
1. Style of this website can be improved to another level, I have written very less CSS, most of the time I used bootstrap template. Anyone can add custom CSS to improve the styling.
2. Frontend user experience can be improved by using javascript framework or vanilla javascript.
## Data Source
1.https://www.imdb.com/ for getting all movie information.
