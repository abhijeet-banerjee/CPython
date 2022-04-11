
class CountObjects:

    obj_count = 0

    def __init__(self):

        CountObjects.obj_count+=1

v = CountObjects()
v1 = CountObjects()
v2 = CountObjects()

print('Total objects created = ',CountObjects.obj_count)