'''
create_import_hash_dictionary.py
Description:
    Creates a dictionary of import names and import hashes based on a custom algorithm to create the hash.
Author: TGZ
Version: 0.0.1
Date: 15 Apr 2019
Sample hash: 304115CEF6CC7B81F4409178CD0BCEA2B22FD68CA18DFD5432C623CBBB507154

Usage:
    Modify algorithm in custom_getHash as required.
    Currently this is only used as a helper script because after creating the dictionary, we do not use it for anything (although we can call searchHash() in the script).
Note:
    Stopped development in this script after I realized there can be functions that IDA does not see it statically in the imports list, but once kernel32 is loaded the malware can access it. So either we need to have the full range of functions in kernel32 statically in an array or we need to do this dynamically.
'''

def custom_getHash(name):
  hash = 0;
  for i in xrange(0, len(name)):
    hash = hash * 31;
    hash = hash + ord(name[i]);
  hash = hex(hash)[-9:-1]; # Get last 8 hex bytes of the int without the "L" (long) character
  return hash;

# searchHash("2398D9DB"); = "WriteFile"
# searchHash("zzz"); = "not_found"
def searchHash(hash):
  for key in import_dictionary:
    search_key = hash.lower();
    if search_key in import_dictionary:
      return import_dictionary[search_key];
  return "not_found";

def imp_cb(ea, name, ord):
  hash = custom_getHash(name).lower();
  import_dictionary[hash] = name;
  return True
  

import_dictionary = {};
nimps = idaapi.get_import_module_qty()

for i in xrange(0, nimps):
    name = idaapi.get_import_module_name(i)
    idaapi.enum_import_names(i, imp_cb)

print import_dictionary
print searchHash("2398D9DB"); # prints "WriteFile"
print searchHash("B5BC68D4"); #MoveFileA but it sends "not_found" because it is not imported!

# Now our dictionary is complete and we can search it
