# "Cybersecurity in microgrids"
In this project you can find a model to diagnose the level of cybersecurity in a microgrid.
+ For starting the project locally **you need to clone the code**, for that open a new console in your computer (We recommend to use Pycharm and work from the "Terminal window") and paste the code bellow to clone the code from this repo into your computer:

```
git clone https://github.com/juliojm13/cybersecurity.git
```
After cloning the code, there must be a directory named "cybersecurity" in your computer if everything went okay, you can check it with this command:

For Linux/Mac:
```
ls
```
For Windows:
```
dir
```
If you can see the directory "cybersecurity", now you have the code to run the project locally! :D

**Now let's run the project**, for that:

- We need to create a virtual environment (venv), do this command: 
    - For Windows:
    ``` 
    python -m venv venv 
    ```
    
    - For Linux/Mac:
    ```
    python3 -m venv venv
    ```
- After that activate the virtual environmen 'venv' with this command:

```
source venv/bin/activate
```

If the activation went okay at the begining of the string in the console there must be a text *(venv)* like this:

```(venv) user@user-VirtualBox:~/Desktop/projects/cybersecurity```

Great! We are almost done!!

+ Then we have to go to the "cybersecurity" folder, for that run this command:

```
cd cybersecurity
```
Now we are in the project directory, by doing the next command we can see our files, pay attention that there **must** be a **manage.py** and **requirements.txt** files:

For Linux/Mac:
```
ls
```
For Windows:
```
dir
```

If you can see our **manage.py** and **requirements.txt** files, then lets install all the libraries that are needed for the project with this command:
```
pip install -r requarement.txt
```

After installing, we can finally run locally our project, use:
For Windows:

```
python manage.py runserver
```

For Linux/Mac:
```
python manage.py runserver
```
Now the project is runing!
You can click the link in that is in the console to open the project in the browser (ussually is this one: http://127.0.0.1:8000/)

Enjoy! ^_^
