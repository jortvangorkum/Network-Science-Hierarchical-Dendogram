### How to install
#### Prerequisite
Extract all the files inside the "datasets" folder.

#### Install project dependencies
The easiest way to use this project is to install `pipenv`.

`pipenv` is a package manager for `pip` so you do not have to manage the dependencies. To install `pipenv` run:
```
pip install pipenv
```
When `pipenv` is installed, run:
```
pipenv install
```
It will install all dependencies needed for this project. When all the dependencies are installed.  Then run:
```bash
pipenv shell #Starts the virtual environment where the dependencies are installed and the correct Python version is specified
python main.py
```
