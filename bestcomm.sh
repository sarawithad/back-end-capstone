# find . -path "/djangazon/website/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
# find . -path "/djangazon/website/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
# rm db.sqlite3; #deletes the database file.
rm -rf APIbestival/migrations; #deletes the migrations folder.
python manage.py migrate; #run the initial django migration to create all the initial tables. need this step because we are killing the database just above
python manage.py makemigrations APIbestival; #creates the migration.
python manage.py migrate APIbestival; #runs the migration.  This will delete all of the data in your database.
python manage.py loaddata genres.json  artists.json dates.json locations.json festivals.json #loads the data from each .json file in sequential order.