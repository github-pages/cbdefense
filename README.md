# Carbon Black Defense API Script
This is a python script used to query for events and write them to a log file so it can be ingested into a log aggregation solution to build alerting around events.

## Getting Started
I suggest creating a python virtual environment as to not screw up local installed python versions/packages

### PreReqs
```
pip install virtualenvwrapper
```
or
```
pip3 install virtualenvwrapper
```
This will install the pip package virtualenv which is used to create the virtual environments.

Next we will create a folder to host all our virtualenvs
```
cd && mkdir .virtualenvs
```
This will place a hidden folder in the root/home directory called .virtualenvs

Now we're ready to create our first virtual environment
```
cd ,virtualenvs && python3 -m venv whatever_you_want_to_name_the_project
```
Now we're ready to change into the virtualenv
```
workon whatever_you_named_the_project
```

WILL FINISH LATER
