import math

class Rectangle():

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

r = Rectangle(4,2)
r.SetLength(6)
r.ShowLength()
