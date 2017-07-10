# bestival: API built with Django REST

Am I the only having trouble keeping track of all the music festivals that are available to attend across the US, not to mention the world, every year? I doubt it. With all these options, how do I decide which festival is BEST for ME? Enter bestival. bestival is a music festival curation and recommendation engine that will give you recommendations of the BEST festival(s) to attend based on your personal preferences of artists, genres, location and month of year.

## Getting Started:

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites:

Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django and Django REST framework:

```
pip install django
pip install djangorestframework
```

The bestival API will be consumed by the bestival AngularJS client which may be found [here](https://github.com/sarawithad/bestival-client)

### Installing:

Clone the repo:

```
git clone https://github.com/sarawithad/bestival-API.git
```

Set up script for building database:

```
chmod +x pyscript.sh
```

Build database:

```
./pyscript.sh
```


Run project locally:

```
python manage.py runserver
```

Navigate to local host in your browser:

```
localhost:8000
```

Once bestival API is up and running it will be ready to be consumed by the [bestival client](https://github.com/sarawithad/bestival-client)

## Built With:

* Python
* Django
* Django REST


## Author:

**Dara Thomas**
