'''
next_poc.py
Description:
    Run a list of functions in some list. Not sure of the formal name of this method (if any), but basically similar to how Express/NodeJS uses their next() middleware function.
    See https://expressjs.com/en/guide/using-middleware.html for examples
    The idea is using this kind of framework, we can run a list of custom functions against every single function IDA detects. Or do any other kind of funky stuff where it can get too messy if we are trying to do large amounts of processing.
Author: TGZ
Version: 0.0.1
Date: 21 Apr 2019
Note:
    Remember to watch out for double processing (e.g. rename function sub_401000 to small_sub_401000 and then process again to small_small_sub_401000)
'''

current_function_list_index = 0
reflection_object = Obj()
function_list = ["start", "function_1", "function_2", "function_3"]

def next(current_function_list_index):
  nextFunction = function_list[current_function_list_index] # determine current processing function
  current_function_list_index = current_function_list_index + 1 # increment current processing function
  getattr(reflection_object, nextFunction)("test") # call the current processing function
  if(len(function_list) > current_function_list_index):
    next(current_function_list_index) # call the next processing function, if any

class Obj(object):
  # the first function argument is a reference to "o", which is useless
  def start_processing(reflection_object, arg1):
    current_function_list_index = 0
    print "start function ran"
    next(1)
  def function_1(reflection_object, arg1):
    print "function_1 ran"
  def function_2(reflection_object, arg1):
    print "function_2 ran"
  def function_3(reflection_object, arg1):
    print "function_3 ran"
    

getattr(reflection_object,"start_processing")('argument here')
