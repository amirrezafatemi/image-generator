# image-generator
Hello everyone, this is my first project and I know it's far from perfection, but I will try my best to do better next time.
This is a simple image generator. 
I used replicate library to get an assist from it's models that like flux.dev (which i used in this project, and you can also
use other prefered models you want from https://replicate.com).
Furthermore, I also used flet library (from https://flet.dev) to use a simle UI page.
[I know the UI sucks, but forgive me. I will do better next time]
The mechanism is shallow. When the script executes, it sends the user's prompt to the AI model and before doing any progress, it
checks if the REPLICATE_API_TOKEN is validate and setting up billing steps through replicate.com are complete. Afterwards, it
gets the result in .webp format.
# Getting Started
Before running the script, you should have these librarys installed on your system:
os, flet, replicate, requests
. The runing version of these packages on my system are listed below .
  Python (-> current verion on my system 3.13.2 on Feb 4 2025)
  replicate (1.0.4)
  requests  (2.32.3)
  flet      (0.27.6)
# Contribution
What I really need from you guys is that you could give a hand in :
  .Fixing bugs
  .Recommending Better Features
  .Designing UI Better
And there is something I am unable to do in this program and that is sending requests to chatgpt or other AIs (perferbly
free) and gettong the image from that. I appreciate if any of you could help me in this part of the program.
