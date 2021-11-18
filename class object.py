from typing import NewType


class grade4():
    name = "deepa"
    age = 30
   #get attribute method(inbuild)
print(type(grade4))
print(getattr(grade4,'name'))
print(getattr(grade4,'age'))
print(getattr(grade4,'gender',"No such attribute found"))
print(grade4.name)
print(grade4.age)
setattr(grade4,'name',"Atul")
print(grade4.name)
setattr(grade4,'gender','male')
print(grade4.gender)
#grade4.city = 'kulasekharam'
#print(grade4.city)
setattr(grade4,'city','Kulasekharam')
print(grade4.city)
print(grade4.__dict__)
delattr(grade4,'city')
print(grade4.__dict__)