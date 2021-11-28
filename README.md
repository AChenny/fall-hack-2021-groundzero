# fall-hack-2021-groundzero

## Wikipedia Chain
- [Simon_Fraser_University](https://en.wikipedia.org/wiki/Simon_Fraser_University)
- [Vancouver](https://en.wikipedia.org/wiki/Vancouver)
- [Vancouver#Sustainability](https://en.wikipedia.org/wiki/Vancouver#Sustainability)

# Using Ground Zero
**Requires At Least Python 3.8**

Clone this repository to your computer and set up a python virtual environment

# Building Ground Zero
`Ground Zero` was developed with Python version 3.10. Development was set up with `virtualenv` in order to manage dependencies an enable future development. To develop, clone this repository and follow the steps below for setting up a python virtual environment.

## Seting up a Virtual Environment
To check if you already have `virtualenv` run this command:
```
py -m virtualenv --version
```
To install `virtualenv` run this command:
```
py -m pip install virtualenv
```
1. Using cmd/powershell or bash terminal, navigate to the top level of this repository
2. Create the virtual environment's directory (venv) with this command:
    ```
    py -m virtualenv venv
    ```
3. Run the activate script to change your terminal's environment to the virtual one.  For cmd/powershell run:
   ```
   venv\Scripts\activate.bat
   ```
   For bash terminal run:
   ```
   source ./venv/Scripts/activate
   ```
   Note that you __must__ run the activate script every time you wish to work on this application in a fresh terminal window.

4. Install the required libraries using:
   ```
   py -m pip install -r requirements.txt
   ```


# Building Ground Zero  
    ```
    django manage.py runserver 127.0.0.1:8000
    ```
