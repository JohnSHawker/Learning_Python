import sys

class Foo:
    def __init__(self, bar):
        self.bar = bar
    def baz(self):
        return self.bar
foo = Foo(12)
print(foo.baz())
print(type(foo))
print(type(foo.baz()))
        
test_file = sys.argv[1]
lin = 0
characters = 0
print(type(test_file), "HERE IT IS!")
with open(test_file, "r") as input_file:
  print(type(input_file))
  lines = input_file.readlines()
  print(type(lines))
  print(lines)
  lin = len(lines)
  for line in lines:
    for char in line:
      characters = len(char) + characters
  print(f"{lin} lines")
  print(f"{characters} characters")
