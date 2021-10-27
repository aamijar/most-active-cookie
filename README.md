# most_active_cookie

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

## Project Structure
