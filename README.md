# ThePokemen

## Roster
- Logan Fu: Project manager, Python/Django views, database design/implementation
- Jonathan Yap: Javascript
- Marcus Negron: CSS, Bootstrap
- Calvin Pun: HTML, templates

## Summary
The purpose of this website is to search, retrieve, store, and display Pokemon data. Detailed information is on the home page,
inserting and displaying Pokemon data is on the Pokedex app, and information about Pokemon type data is on the Battle app.

## API Used
https://pokeapi.co/

## Launch Codes
1. Make pyenv in the Project repo:
- pyenv local 3.11.5
- python -m venv env_3.11.5
2. Install packages with pip install:
- pip install --upgrade pip-tools pip setuptools wheel
- pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
- pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in
- pip-sync requirements_env/main.txt requirements_env/dev.txt
3. Go to ../ThePokeymen/pokemon/pokemon and make a secrets.json file
- Follow the format in secrets_template.json
4. Go to ../ThePokeymen/pokemon
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py runserver
5. Go to 127.0.0.1:8000/pokedex
- Load initial data using the initial data button (this may take some time)
- The app is now ready to use!
