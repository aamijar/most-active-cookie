# most-active-cookie
[![pytest_run workflow](https://github.com/aamijar/most-active-cookie/actions/workflows/pytest_run.yml/badge.svg)](https://github.com/aamijar/most-active-cookie/actions/workflows/pytest_run.yml)

Command line program to process log file and return the most active cookie

## Project Spec

* Cookie log file format - csv
* Define the most active cookie as one seen in the log the most times during a given day

Assumptions:
* If multiple cookies meet criteria, return all of them on separate lines
* -d parameter takes date in UTC time zone
* You have enough memory to store the contents of the whole file
* Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file)

## Run Steps

Quick Run:
```
$ python3 most_active_cookie.py cookie_log.csv -d 2018-12-09
```

Executable and Run:
```
$ chmod +x most_active_cookie
$ ./most_active_cookie cookie_log.csv -d 2018-12-09
```

## Environment

**Python3 + Pytest**

Virtual Environment [Optional]:

Ex: Miniconda

```
$ conda create -n cookie python
$ conda activate cookie
```

Install Pytest via pip:
```
$ pip install pytest
```

Save environment:

```
$ conda env export > environment.yml
```
```
$ pip freeze > requirements.txt
```

## Testing

At root of project use pytest

```
$ python3 -m pytest
```

## Project Structure

* /cookie - datatypes to hold cookie[s] and find most active
* /parsing 
    * read cli arguments and read log file lines
    * filter log file content based on cli arguments (ex. UTC Date) using binary search
* /timeutil - helper functions to determine date and time from UTC format
* /testing - pytest based tests to validate program functions
