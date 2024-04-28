import numpy as np

def is_prime(n:int) -> bool:
  if n < 2:
    return False
  else:
    for i in range (2, int(round(np.sqrt(n)+1,0))):
      if n%i == 0:
        return False
    return True

if __name__ == "__main__":
  print(is_prime(6.2))
  print(is_prime.__annotations__)