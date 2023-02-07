# Go to page, login, refresh on repeat
Student myTimetable tool delayed the allocation openings from 9AM to 11AM. 

Before they announced the new 11AM time, I contemplated about a webdriver program to 
regularly refresh the page and check the status of the alert. Well, they anounced the 11AM time pretty
quickly, so I didn't set up any sort of notification system -- but it printed regularly to console. Think I ended up running it from 10:30-11:00.

I found the web design hardly used ID's or easier identifiers so I just got lazy and copy-pasted the X-Paths to find elements (Ctrl+Shift+I tools for the win).

Also, EdgeDriver is super weird? In some scenario I might've used ChromeDriver instead for better googleability support-wise, but I don't have Chrome installed :P

Sloppy code, several print statements, and no terminating goal :D