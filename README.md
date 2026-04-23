# Project Template
This is a boilerplate project setup for you to get started! Feel free to customize/rename/delete anything 🙂

## On the Structure
* `docs` contains your project documentation (e.g. your planning meetings, but also any diagrams or requirements documents you would like to keep track of centrally).
* `project` contains most Python source files and tests.
* `main.py` is the entry point to your application, use it only to call/launch functionality from `project`.

## Setup
* Have Python 3 installed
* Download and run PyCharm Education
* Select `Check out from Version Control` > `Git` > enter your project GitLab project URL
* `Would you like to open the directory?` > `Yes`
* A couple of configurations once you're inside:
    * Go to `File` > `Settings` > `Project` > `Project Interpreter` > `Show all` > `Add (+)` > `Virtualenv Environment` > Select a version of Python as `Base Interpreter` > `OK` (3 times)
    * Go to `File` > `Settings` > `Tools` > `Python Integrated Tools` and change the default test runner to be `pytest`
    * Open `requirements.txt`, and in the yellow popup that appears, click on `Install requirements`

## Running
In PyCharm, run `main.py` by opening it and hitting the green play button.

## Testing
To run all tests, right-click on the `project/test` folder and select `Run 'pytest in test'`. To run an individual test, click on the green play button next to it.

You can also do the same through the terminal (open it in PyCharm by clicking on `Terminal` in the lower toolbar - you may have to click on the icon in the bottom-left corner to reveal it):

```
pytest project
```

## Coverage
Run the following command (from within the PyCharm terminal) to record coverage:

```
pytest --cov-config=.coveragerc --cov=project --cov-report=html project/test
```

The output goes into the `htmlcov` directory. You can view your coverage report by right-clicking on the `index.html` file in that directory and selecting `Open in Browser`!

## Pylint
Run `pylint` to check for code style violations by running the following command (from within the PyCharm terminal):

```
pylint project
```
# Alcohol-Accountant
