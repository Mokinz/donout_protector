# donout_protector

TL/DR: Small python script that locks your screen as you go afk

As I was bored at work I started a small pyhon project.

In our company whenever sombody does not lock their laptop, anybody has a right to send an email to all employees, that afk person will bring donuts to office soon.
Of course it is a security issue and I am always stressed about it. So I got an idea - create a script that checks if I am in front of the laptop and when not - it locks it! Simple enough.

I managed to programm such thing and for now it has main funcionality but it's not polished yet. I plan to develop this project only when I am bored at work and feel like it.

Program works like this:

Step 1. Run a program through console.

Step 2. GUI opens up. Click on Run script.

Step 3. Now, every 5 seconds prgoram looks through your camera in laptop and checks if you're looking towards it. If you're head is turned around or your not in the camera frame then scrpt locks the screen and turns off.

That's all!

Of course program is quite primitive beacuse it has several flaws:

1. This does not specifically detects you but any face. So if two people are looking in the direction of the laptop, script will not work until both people look away.
2. You need to manually start the script every time you start computer and log in to your account.
3. Ideally it should start evry time computer is switched on and run in the background.
4. There is no need to turn on the camera every 5 seconds while typing or clickig. 

In future versions I'll try to fix those flaws but still I think that is useable version that's why I am posting it.

