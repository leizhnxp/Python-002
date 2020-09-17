from homework02 import copycat_map

def test_copycat_map():
  func = lambda x:x+1
  list_numbers = [1,2,3,4,5]
  expect = map(func, list_numbers)
  actual = copycat_map(func, list_numbers)
  assert sum(expect) == sum(actual)

