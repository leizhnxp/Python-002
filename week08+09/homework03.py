import datetime


def timer(func):
  def timer_wrapper(*args, **kwargs):
    start = datetime.datetime.now()
    result = func(*args, **kwargs)
    print(datetime.datetime.now()-start)
    return result
  return timer_wrapper


@timer
def wokao(x):
  print("wolegequ",x)


@timer
def woqu(x,y):
  print("wolegequ",x,y)


wokao("wokao")
woqu("wo","qu")

