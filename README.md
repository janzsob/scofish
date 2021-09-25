# Scofish
It's a web application where fishermen can record their catches and compete with each other.

Scofish was built to make life easier for fishermen. Memories will never be lost. They can look back at any time to see what tricks worked. The web application provides some useful statistics about users performance.

This is my first project that is deployed publicly and has some active users.

## Functionality
* User authentication: registration, login. Authentication is required in case of creating and editing objects.
* Password reset: if users forget their passwords, they can claim password reset by giving their email.
* There is a contact page where users can send messages to the admin. Messages arrive at the admin's email address.
* Users can create their own fishing trips. They can select the duration of the trip in a calendar. Other users can also be added to the trip.
* Catches can be recorded within trips. Users can give the fish weight and upload images.
* Each trip has a statistics page that summarizes the catches, ranks fishermen based on the amount of catches, displays a diagram about the used hook baits.
* There is a profile page where users can see their own trips, catches and hook baits.
* On the home page there is a timeline where all trips are listed.


## Technologies
* Python 3.8
* Django 3.1
* PostgreSQL
* Bootstrap 5
* HTML 5 and CSS
* jQuery 3.6
* Chart.js
* flatpickr 4

## Deployment
The project is hosted on Heroku.

https://www.scofish.net/
