def main(n):
  sum = 0
  for i in range(n+1):
    sum += i*i
  return sum

print(main(5))