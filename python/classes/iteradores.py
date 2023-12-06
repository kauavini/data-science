mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"

for x in mystr:
  print(x)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if(self.a <= 20):
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



class Iteravel:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        self.a += 1
        return self.a


myclass = Iteravel()
myiter2 = iter(myclass)

print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))