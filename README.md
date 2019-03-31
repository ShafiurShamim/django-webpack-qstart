## Django Webpack Quick Start

### Installation

Requirements

- Python 3.6

```sh
# Install virtualenv if you don't have
pip3 install virtualenv

# Create a virtual environment
virtualenv my-env

# Activate the virtualenv
source my-env/bin/activate

# Clone the git repository
git clone https://github.com/ShafiurShamim/django-webpack-qstart.git

# Change directory into the project directory
cd django-webpack-qstart

# Copy or rename file config.example.json to config.json
cp config.example.json config.json

# Install dependencies
pip install -r requirements.txt

# Create tables
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

```

### Webpack Installation

Requirements

- [Node.js](https://nodejs.org)

```sh
# Install dependencies
npm install

# Compile scss and javascript
npm run dev
# or
npm run prod
```

### Finally run the server

```sh
python manage.py runserver
```

