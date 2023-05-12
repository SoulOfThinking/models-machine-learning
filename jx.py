import math

class Rectangle(object):


      def __init__(self, length, width):
          self.length = length
          self.width = width

      def SetLength(self, length):
          self.length = length

      def SetWidth(self, width):
          self.width = width

      def ShowLength(self):
          print(self.length)

      def ShowWidth(self):
          print(self.width)

      def GetArea(self):
          return (self.length * self.width)

r = Rectangle(6,7)
r.ShowLength()
r.SetLength(6)
r.ShowLength()
print(r.GetArea())
