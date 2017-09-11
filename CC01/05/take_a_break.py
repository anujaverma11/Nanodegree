# Open a browser and open the given URL. Using Python function Time and Webbrowser

import time
import webbrowser

total_breaks = 3
break_count = 0

while(break_count < total_breaks):
    time.sleep(1800)
    webbrowser.open("https://www.youtube.com/watch?v=spD7G1uKBLQ&list=PLW2U16DvmuMHiX7tqZadS_sfo55WbDjuR")
    break_count = break_count + 1