import pizero_2relay as pizero
from time import sleep


r1 = pizero.relay("R1")
r2 = pizero.relay("R2")

r1.on()
sleep(2)
r1.off()
sleep(2)

r2.on()
sleep(2)
r2.off()
sleep(2)
