# # # IMPORTS
#
from time import sleep 
  #--control length of pin pulses (on/off, high/low), &c.
import sys
  #--
import RPi.GPIO
  #--control Raspberry PI GPIO pins
import math # math.sqrt
  #--Calc'ing the belt lengths using PythagTheorem

import spider
  #--contains the Plotter class
#
# # # 
  
#--Instantiate plotter class instance
webster = spider.Weaver(
  #--Width of motors:
  
  #--Height of drawing-wall:
  
  #--**kwargs
  
  #
  )
  

  
#
#
#--Set SPIDER in motion, get weaving! ... er, drawing!
for point in path:
  webster.move  (  )
  
