'''
Author: TGZ

Notes:
    One extremely important thing to take note of is that Appcall does not follow the rules of breakpoints.
    The function will just silently run fully even if there are software/hardware breakpoints.
'''

# Version 1 (All functions working, assuming the return value is available as a string)
testfunc = Appcall.proto("kernel32_GetCommandLineA", "int kernel32_GetCommandLineA();");
address_result = testfunc();
string_result = GetString(address_result, -1, ASCSTR_C);
print string_result;

# Version 2 (Windows API functions only)
x = Appcall.GetCommandLineA();
print x;

# Version 3 (All functions working)
proto = "signed int sub_10002DD8();"
anyfn = Appcall.proto(0x10002DD8, proto);
anyfn();
