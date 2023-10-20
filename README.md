# install

LINUX ONLY

before proceeding with installation you must install [pyenv](https://github.com/pyenv/pyenv) in order to use the correct version of python interpreter, and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) to create virtual environments.

clone this repository in a location of your choice and navigate to the cloned directory.

```bash
git clone -b v0.0.1 https://github.com/sesheii/flasklab.git
```
```bash
cd flasklab
```

open a terminal in the parent directory and run these commands.

```bash
python -m virtualenv venv
```

```bash
source venv/bin/activate
```

```bash
python -m pip install -r requirements.txt
```

# run

Run this command in terminal in the parent directory in order to start the [gunicorn](https://gunicorn.org/) server in debug mode. 
In arguments of this command the number of workers (threads) is set to 4, server is run on localhost on port 5000.

```bash
gunicorn -w 4 -b 0.0.0.0:5000 --reload --chdir ./app app:app
```

Or navigate to ./app directory and run this instead

```bash
flask --app app run
```