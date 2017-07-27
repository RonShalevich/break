import webbrowser
import time

total = 2
counter = 0

print("This program started on "+time.ctime())
while (counter < total):
    time.sleep(2*60*60)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    counter = counter + 1
