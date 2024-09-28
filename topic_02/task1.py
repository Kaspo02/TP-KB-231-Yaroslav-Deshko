from math import sqrt


def discriminant(a: float, b: float, c: float) -> float:
    return pow(b, 2) - 4*a*c


def findRoots(a: float, b: float, c: float):
  d = discriminant(a, b, c)

  if d == 0:
     return [-(b/2*a)]
  elif d > 0:
     return [((-b)+sqrt(d))/ 2*a, 
             ((-b)-sqrt(d))/ 2*a ]  
  return None


def test():
  print(findRoots(1, 2, 2)) # D < 0
  print(findRoots(1, 2, 1)) # D == 0
  print(findRoots(1, 5, 1)) # D > 0
  
  
test()