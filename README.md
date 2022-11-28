# flask API for Editing Images
This project was created with flak framework which is built on python language

## __getting started__
<br/>

### <mark style="background-color: whitesmoke;font-weight: bold;padding: 4px">1- creating a virtual environment</mark>

<br />

> first we need a virtual environment with python.

In windows we can write this command in the terminal inside root directory: 

```
python -m venv venv
```

and for linux and macOS (also inside the root directory):
```
python3 -m venv venv
```

### <mark style="background-color: whitesmoke;font-weight: bold;padding: 4px">2- activating the virtual environment</mark>

<br />

>second we want to activate this virtual environment.

for windows we can activate it by running this command in the same directory that __virtual environment__ has:
```
venv\Scripts\activate
```

and for linux and macOS:

```
source venv/bin/activate
```

 ### <mark style="background-color: whitesmoke;font-weight: bold; padding: 4px">3- installing dependencies</mark> 

<br/>

> Then we should install the required modules for this project by running this command __when the virtual environment is activated__.

```
pip install -r requirements.txt
```

 ### <mark style="background-color: whitesmoke;font-weight: bold; padding: 4px">4- running the site</mark> 

<br/>

> We an run the site by running this command.

```
flask run
```

and if we want to activate the DEBUG mode we run this __before running the site__
```
set FLASK_DEBUG=True
```

then we can access the site through http://127.0.0.1:5000.

 we can deactivate the venv by running this command:
 ```
 deactivate
 ```
