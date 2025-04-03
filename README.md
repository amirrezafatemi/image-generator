# image-generator 🖥️
Hello everyone, this is my first project and I know it's far from perfection, but I will try my best to do better next time.
This is a simple image generator.

I used replicate library to get an assist from it's models that like flux.dev (which i used in this project, and you can also
use other prefered models you want from [replicate](https://replicate.com) library.

Furthermore, I also used [flet](https://flet.dev) library to use a simle UI page.

*I know the UI sucks, but forgive me. I will do better next time*

The mechanism is shallow. When the script executes, it sends the user's prompt to the AI model and before doing any progress, it
checks if the REPLICATE_API_TOKEN is validate and setting up billing steps through replicate.com are complete. Afterwards, it
gets the result in .webp format.
# Getting Started ⚡
The current version of my python which I tested my program is 3.13.2.

Before running the script, you should have these librarys installed on your system:
os, flet, replicate, requests.

The runing version of these packages on my system are listed below :

  + replicate
  
  + requests
  
  + flet
# API Reference
[Black Forest Labs](https://blackforestlabs.ai/)

I used this API whith [replicate](https://replicate.com).

Note: Sign up for an API token key and add it to [image-generator.py]
# Installation 📚
Before starting the image-generator.py, run:

```bash
pip install -r requirements.txt 
```

Or you can install each package manually via your command line:

```bash
pip install replicate
pip install requests
pip install flet
```
## Running The Program
1.Download the zip format of file, or run the following code
 ```bash
git clone https://github.com/amirrezafatemi/image-generator.git
```

1.Do not run, but open the image-generator.py in an editor

2.Replace your token with the YOUR_TOKEN_API

3.Then run image-generator.py

4.Write your prompt which describes your desired image to generate

5.Click on the generate image

6.The image will be created
# Contribution ✨
What I really need from you guys is that you could give a hand in :

  -**Fixing bugs**
  
  -**Recommending Better Features**
  
  -**Designing UI Better**
  
*And there is something I am unable to do in this program and that is sending requests to chatgpt or other AIs (perferbly
free) and gettong the image from that. I will work on it to try other free methods to use AI sufficiently.*

*The reason is that we as people need the AI anywhere and anytime to be available, and so it wouldn't be a hassle for us if it was free out of charge.*

*Also, I will try to fix the UI. You may ask why?*

*The reasons are rudimentry. It is not possible to change the Icon on everyone devices. Also, beside that one, I personally want to use another UI editor library to make it better. I am not saying that the flet library is bad; However, this was my first time designing user interface.*

I appreciate if any of you could help me in this part of the program.
