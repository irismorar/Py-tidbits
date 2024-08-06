def self_math(math_func):
  def inner_func(x):
    return math_func(x,x,x)
  return inner_func

def multiply(x, y, z):
  return x * y * z

def add(x, y, z):
  return x + y + z

tripple_mult = self_math(multiply)
tripple_add = self_math(add)

print(tripple_mult(3.5))
print(tripple_add(5))

