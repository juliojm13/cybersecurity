# The project "Cybersecurity"
+ For starting find a green botton that names *Code*. Click it and copy link from this.
+ Create some empty folder for your project in your Desktop and open this folder with using PyCharm
+ Next step: choose the window *Terminal* in Pycharm and check if you located in your new folder.
Then you need to do this command with copied link (we are cloning repo):

```git clone https://github.com/juliojm13/cybersecurity.git```
- We need to create a virtual environment (venv), do this command: 
    - For Windows: ``` python -m venv venv ```
    - For Linux/Mac:```python3 -m venv venv```
- Will activate venv:
```source venv/bin/activate```

After this movement you have to see a text *(venv)* in starting of string like this:
```
(venv) polina@polina-VirtualBox:~/Desktop/daniala/cybersecurity
```
+ Then we will change folder but first of all check available folder. Use
command: ```ls```

You must see a folder *venv*, a folder with our project *cybersecurity*
and file *README.MD* or something like that) Okey change folder. Use:
```cd cybersecurity```.
The path in command string have to change to neccessary folder.
+ Now we need to install every apps that neccessary us in this project for that we need to find a 
file *requarement.txt*. It has to be in the same folder where we are. Check it: ```ls```. Then install every apps:
```pip install -r requarement.txt```
+ After installing, we finally can open locally our project. Use: ```python manage.py runserver``` 


