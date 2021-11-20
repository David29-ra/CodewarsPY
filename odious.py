
import re
def evil(n):
  return "It's Evil!" if (len(re.findall("1",format(n, "b"))) % 2 == 0) else "It's Odious!"

# def evil(n):
#   return "It's Evil!" if len(format(n, "b").replace("0", "")) % 2 == 0 else "It's Odious!"

# def evil(n):
#   return "It's %s!" % ["Evil","Odious"][format(n, 'b').count("1") % 2]

print(evil(13))