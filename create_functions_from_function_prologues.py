'''
create_functions_from_function_prologues.py
Description:
    Create functions from all function prologues found (e.g. "55 8b ec"). Also prints out the function address found if it created a function.
Author: TGZ
Version: 0.0.1
Date: 15 Apr 2019

Note:
    Can be made more extensible if we change the search+makefunction into a separate function which can be called. Then, we can send e.g. create_from_prologue("55 8b ec"; create_from_progloeu("8b ff 55 8b ec");, or even e.g. go backwards from "55 8b ec" all the way until we see a "retn" and then CreateFunction from the next instruction after that.
    
Reference for find_string_occurrences(string) function : https://unit42.paloaltonetworks.com/using-idapython-to-make-your-life-easier-part-5/
'''

def find_string_occurrences(string):
  results = []
  base = idaapi.get_imagebase() + 1024
  while True:
    ea = FindBinary(base, SEARCH_NEXT|SEARCH_DOWN|SEARCH_CASE, string)
    if ea != 0xFFFFFFFF:
      base = ea+1
    else:
      break 
    results.append(ea)
  return results
  
function_prologue_list = find_string_occurrences("55 8b ec");
for function in function_prologue_list:
  if not GetFunctionName(function):
    MakeFunction(function);
    print function;
