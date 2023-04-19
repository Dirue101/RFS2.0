# RFS2.0
My second iteration of a random fight generator
A random fight generator utilizing chatGPT, and google tts API to do most of the grunt work.
This code consistently generates voice acting, and semi consistently generates voice acting with different voices. Due to chatgpt generating scripts inconsistently, much more work needs to be done before it is working 100%. This is all located in formatScript.
flaskApp contains three flask websites that operate based on a json passed in on the main app. There is a working teleprompter, a page that opens up and plays a music clip on loop, and the fight screen, which runs while the api is creating the script and generating the voiceacting. teleprompter would work perfctly, but i need to pass the tts audio length, and divide by script content size to calculate scroll speed, and i havent been able to work on it. 



There are several hard-coded variables you need to change to get this operational on your system, 
you also have to have google api thing working on your pc
web browser path in assembleFight

Backup destination in backupcleanup

several paths in formatScript

I will work on making this available to change in an options folder soon.
after that, assembleFight should automatically construct pages, and read them aloud
##################################### TO DO #############################################



Fix voice generation for all script cases

implement an SQLite database locally, so it is more reliable, and less reliant on hard coded variables

pass audio length to js code for teleprompter to accurately calculate scroll speed.

expand on prompt generation, fight types, size, combatant number and more

get more stock fight music, to change it up a little

animate fightscreen to provide a better visual element

eventually work on procedural animation (long shot)
