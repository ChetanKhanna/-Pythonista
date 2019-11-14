# Descriptors

+ if an object declares a method called __get__, python won’t return the object itself when accessed, but the result of its __get__.

+ Descriptors can define custom behavior when class attributes are being accessed, modified or deleted.

+  data descriptors have higher precedence than instance variables


I was going through articles on discriptors, but none of them seemed to be really hitting the point.
Until I stumbled upon this beautiful piece by [Pablo Arias](https://pabloariasal.github.io/2018/11/25/python-descriptors/)

Some references:

+ [what are those params in __get__ and __set__ ?](https://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors)

+ [another good article](https://dzone.com/articles/python-201-what-are-descriptors)

+ [Official Python docs on descriptors](https://docs.python.org/3/howto/descriptor.html)


Hope it helps!