def is_square(arr):
  if arr: return all(list(map(lambda x: (pow(x, 0.5).is_integer()) ,arr)))

# def is_square(arr):
#   if arr:
#     return all((a ** 0.5).is_integer() for a in arr)

# def is_square(arr):
#     return None if len(arr) == 0 else all(list(map(lambda x: (pow(x, 0.5) % 1 == 0) ,arr)))

print(is_square([1, 4, 9, 16]))

print(is_square([3, 4, 7, 9]))

print(is_square([]))
