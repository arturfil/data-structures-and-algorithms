
# Creating and Implementing the dynamic array ourselves using the 
#   c type library built in and using objects with public and private methods
import ctypes

class M(object):
  def public(self):
    print("Use Tab to see me (I'm public)")

  def _private(self):
    print("I'm a private method that should'nt be acccesible for everyone")

m = M()
m.public()
m._private()