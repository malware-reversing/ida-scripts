'''
load_arbitrary_dll.py
Description:
    Loads arbitrary DLLs into your running executable. This is a simpler version compared to running rundll32.exe but was made for the benefit of merging contents of multiple files (e.g. decryptor function in file x loading file y and decrypting file y contents).
Author: TGZ
Version: 0.0.1
Date: 12 May 2020
'''

LoadLibraryA = Appcall.proto("kernel32_LoadLibraryA", "HMODULE LoadLibraryA(LPCSTR lpLibFileName);")
GetLastError = Appcall.proto("kernel32_GetLastError", "DWORD GetLastError();")

dllname = "dllname.dll"

hinstLib = LoadLibraryA(dllname)
error = GetLastError()
if error:
  print("Failed with error code: " + str(error))
else:
  print("Success, handle# is: " + str(hinstLib))
