from collections import namedtuple

vector = namedtuple("Dimension",'x y z')
vec_1 = vector(1,1,1)
vec_2 = vector(1,0,1)

manhattan_distance = abs(vec_1.x - vec_2.x) + abs(vec_1.y - vec_2.y) \
                            + abs(vec_1.z - vec_2.z)
                            
print "Manhattan distance between vectors = %d"%(manhattan_distance)