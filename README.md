# House Manager

Aka. John The Fish

This is a Django application that I wrote to manage the bills, people, and other associated things for my shared house. I deemed it necessary to help reduce the logistics of sharing information between eight different people.

## Features

### Current

- People management
- Bills & Services management, including what people in the house need to pay

### Upcoming

- House Documents
- Facebook messenger integration
- Teller API Integration

## Setting Up

This is a standard Django application, so the setup steps are pretty standard.

- Clone the repository
- Install the dependancies using `pipenv install && pipenv shell`
- Populate `house.yml` with the details of your house
- Migrate the database `./manage.py migrate`
- Create a superuser `./manage.py createsuperuser`
- Start the dev server `./manage.py runserver`

## Licence

This software is licensed using GNU GPLv3, see the `LICENSE` file for more details.
