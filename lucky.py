def filter_lucky(lst):
  return list(filter(lambda n: (str(n).find('7') != -1) ,lst))

# def filter_lucky(lst):
#   return [n for n in lst if '7' in str(n)]


print(filter_lucky([1,2,3,4,5,6,7,68,69,70,15,17]))