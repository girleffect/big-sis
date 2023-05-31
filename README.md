A Wagtail project build with docker and hosted on Divio's cloud infrastructure
-----

## Project structure

Apart from the regular files created by Django/Wagtail this repository contains:

```
addons              - Python/Django applications that have been packaged for easy deployment on Divio
apps/
├── api             - App responsible for the API to get the Services and all their information. Used by the Big Sis Chatobot.
├── blog            - App responsible for the the Blog section of the website (Wagtail Page types: BlogIndexPage, BlogCategoryPage, PostPage)
├── helpers         - App that includes template tags and helpers used throughout the app and a global settings model.
├── pages           - App responsible for the the Content pages of the website (Wagtail Page types: HomePage, AboutPage, ContentPage)
├── services        - App responsible for the the Services/Clinics database the website (Wagtail Page types: ServiceFinderPage, ServicePage, ServiceType, ServiceLocation)
├── theme           - Third party app (django-tailwind) used for front-end development.
templates/          - Application html files/templates
├── blog/           - Blog app Templates files
├── includes/       - Footer and main navigation template files
├── pages/          - Pages app template files
├── sevices/        - Services app template files
├── 404.html        - 404 Template (currenty empty)
├── 500.html        - 500 Template (currenty empty)
├── base.html       - Base Template
├── robots.txt      - Robots.txt file
├── seo.html        - Template for SEO meta tags
docker-compose.yml  - YAML file defining services, networks, and volumes for a Docker application. 
.env-local          - A file containing enviromental variables used in local development.
Dockerfile          - The dockefile used by our application to assemble an image.
Procfile            - Commands that are executed by the app on startup.
requirements.txt    - List of dependencies

```
## How To:

### Setup the project
**Requirements:** [Docker](https://www.docker.com/) and Docker Compose (Docker Compose is included with Docker Desktop for Mac and Windows).
Open a terminal and follow the below instructions:

```sh
# 1. Build the containers
docker-compose build
# 2. Install frontend dependencies
docker-compose run --rm web python manage.py tailwind install
```
### Run the project on a development machine:
```sh
# 1. Start server
docker-compose up
# Then visit http://localhost:8000 in your browser.
```
### Start front-end development tools and file watching:
```sh
docker-compose run --rm web python manage.py tailwind start
```
### Build front-end assets:
```sh
docker-compose run --rm web python manage.py tailwind build
```
### Deploy project
```sh
# https://docs.divio.com/en/latest/introduction/01-installation/
```
