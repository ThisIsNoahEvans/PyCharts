#!/bin/python3

import pygal

#####                                                                   #####
print('The data displayed is simply for demo purposes: please do not use it.')
#####                                                                   #####

piechart = pygal.Pie()
piechart.add('Pandora', 41)
piechart.add('Gmail', 44)
piechart.add('Google Play', 47)
piechart.add('Snapchat', 50 )
piechart.add('Instagram', 50)
piechart.add('Google Maps', 57)
piechart.add('Google Search', 61)
piechart.add('Facebook Messenger', 68)
piechart.add('YouTube', 71)
piechart.render()

barchart = pygal.Bar()
barchart.add('Windows 7', 49.04)
barchart.add('Windows 10', 26.8)
barchart.add('Windows XP', 6.94)
barchart.add('Windows 8.1', 6.4)
barchart.add('macOS', 3.49)
barchart.add('Linux', 2.36)
barchart.add('Windows 8', 1.37)
barchart.add('Other', 3.6)
barchart.render()
