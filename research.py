from types import MethodType
from notebook import Notebook, Note
from menu import Menu

var = 1
notebook = Notebook()
print(isinstance(var, object)) #True
print(isinstance(notebook.modify_memo, object)) #True
print(isinstance(Notebook, object)) #True
# Object is unique instance of a data structure. All variable, class, method and other is object.


print(isinstance(var, type)) #False
print(isinstance(notebook.modify_memo, type)) #False
print(isinstance(Notebook, type)) #True
# The type of object defined by the programmer in which the set of attributes is described
# characterizing any object of the class.Example of class is Menu or Notebook


print(Menu.__dir__(Menu))
# ['__repr__', '__call__', '__getattribute__', '__setattr__', '__delattr__', '__init__', '__new__',
# 'mro', '__subclasses__', '__prepare__', '__instancecheck__', '__subclasscheck__', '__dir__', '__sizeof__',
# '__basicsize__', '__itemsize__', '__flags__', '__weakrefoffset__', '__base__', '__dictoffset__', '__mro__',
# '__name__', '__qualname__', '__bases__', '__module__', '__abstractmethods__', '__dict__', '__doc__',
# '__text_signature__', '__hash__', '__str__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__',
# '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__class__']
# This all atributes of class Menu. Atributes it is variables within the class that are referenced
# on methods, functions, variables or other classes


menu = Menu()
print(isinstance(menu.__str__, MethodType)) #False
print(isinstance(menu.__init__, MethodType)) #True
# Method are function that belong to class. They can operate not only on data inside function,
# also they can operate on data that is contained within the class

# Argument self - the first parameter is a link per object
# __init__ method to be called for object creation
# __str__ method is standard way of presentation object as a string of characters.
