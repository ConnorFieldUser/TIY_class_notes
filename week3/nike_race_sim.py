
from nike_race import Nike, Footrace

nike1 = Nike(4)
nike2 = Nike(7)
nike3 = Nike(5)


footrace = Footrace(25)
footrace.add_nikes([nike1, nike2, nike3])

while not footrace.has_won():
    footrace.tick()

print("A Nike sponsered competitor has won! {}".format(footrace.winner.acceleration))
