# 放弃多iterable吧

def copycat_map(func, iterable):
  return [func(x) for x in iterable]

