# Social Media Dashboard
This Django project serves as a unified platform to view analytics from various social media sources. It integrates with platforms such as Twitter, Facebook, and more. The project offers custom user authentication and also provides OAuth integration with Google.

## Prerequisites
* Python (>=3.6)
* pip
* Virtual environment (optional but recommended)
* Google Developer Account (for OAuth)
* Getting Started

## Clone the Project
```commandline
git clone git@github.com:indranandjha1993/social_media_dashboard.git
```

## Setting Up a Virtual Environment (venv)
To create a virtual environment:

```commandline
python -m venv venv
```

### Activate the virtual environment:
* Windows:
```commandline
venv\Scripts\activate
```

* macOS and Linux:
```commandline
source venv/bin/activate
```

## Install Dependencies
```commandline
pip install -r requirements.txt
```

##  Environment Variables Configuration
Make a copy of the .env.example file and rename it to .env. Update the variables in .env with your values:

```commandline
cp .env.example .env
```

## Database Setup
After updating your .env with the appropriate database credentials, apply migrations:

```commandline
python manage.py migrate
```

## Google OAuth Setup
1. Visit the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project.
3. Navigate to the OAuth consent screen and configure it.
4. Go to the Credentials tab and click "Create Credentials". Choose "OAuth 2.0 Client IDs".
5. Select "Web application". Fill in the authorized redirect URIs for your Django app.
6. Update the .env file with the provided client ID and secret.
7. Ensure the redirect URIs in the Google Developer Console match the URIs in your Django settings (typically /o/google-oauth2/login/ and /complete/google-oauth2/).

## Running the Server
To start the development server:

```commandline
python manage.py runserver
```