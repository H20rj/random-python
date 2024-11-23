###
# Pixel density calculator. Used for seeing how good a display might look.
# ###
from math import cos, sin
from library import get_monitor_resolution, get_monitor_size, get_lower_left_angle
from time import sleep
#def variables from library
monitor_size = get_monitor_size()
monitor_resolution = get_monitor_resolution()
monitor_angle = get_lower_left_angle(monitor_resolution[0], monitor_resolution[1])


# calculate width, height and pixel density
width = monitor_size * cos(monitor_angle)
height = monitor_size * sin(monitor_angle)
pixels_per_inch = monitor_resolution[1] / height

#print
print(f"Monitor width: {width:.2f} in")
print(f"Monitor height: {height:.2f} in \n")
print(f"Pixels per inch (PPI): {pixels_per_inch:.2f}")
ppi = pixels_per_inch
print()
sleep(0.3)
# Explain PPI
if ppi <= 50:
    print("""Description: Very low-density displays (obsolete or large, old tech).
Usage: Large outdoor displays, vintage monitors, or older industrial screens.
Result: Very noticeable pixels, poor text and image clarity, only usable for basic visuals.
""")
elif ppi <= 100:
    print("""Description: Low resolution
Usage: Basic or older displays, some projectors, budget-friendly large monitors.
Result: Usable for text and simple images, but coarse details; unsuitable for modern HD media or professional work.""")
elif ppi <= 150:
    print("""Description: Standard resolution (common in older laptops and monitors).
Usage: Mid-range monitors, everyday office work, web browsing, casual gaming.
Result: Text and images are clear enough for general use but lack the sharpness needed for fine detail or high-quality visuals.""")
elif ppi <= 200:
    print("""Description: High resolution (modern standard for mid-range monitors).
Usage: Many 1080p or 1440p monitors, laptops, and mid-tier gaming or productivity displays.
Result: Good balance of sharpness and usability; fine for most tasks, but close inspection may reveal pixelation.
""")
elif ppi <= 300:
    print("""Description: Very high resolution (common in premium laptops and displays).
Usage: Retina or 4K displays on laptops, professional monitors, and some tablets.
Result: Text is crisp, and images are sharp even at close distances; ideal for graphic design, photo editing, and detailed work.
""")
elif ppi <= 400:
    print(""""Description: Ultra-high resolution (common on smaller displays like phones).
Usage: High-end laptops, 4K monitors under 24", smartphones, and tablets.
Result: Pixels are virtually invisible to the naked eye at standard viewing distances, offering incredible clarity.
""")
elif ppi > 400:
    print("""Description: Extreme density (found in flagship smartphones and VR headsets).
Usage: Smartphones, high-end tablets, and VR/AR devices.
Result: Text and images are impossibly sharp even under a magnifying glass; perfect for immersive experiences or detailed visuals.
""")

sleep(0.3)

print()
if ppi < 200:
    print("""Reminders:
    Key Notes for Monitors:
    Viewing distance matters: Higher PPI is only noticeable if you're close enough to perceive the difference.
    Most desktop monitors and laptops don't exceed ~220 PPI because beyond that, the improvement in clarity is minimal for standard viewing distances.
    Ultra-high PPIs (300+) are typically reserved for smartphones or small displays where the viewing distance is closer.""")


