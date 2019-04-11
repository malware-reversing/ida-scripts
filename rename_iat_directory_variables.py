/*
 * rename_iat_directory_variables.py
 * Description: When a malware dynamically resolves a new IAT Directory somewhere else, this script renames all variables in the new IAT Directory to the name of where the offsets point to.
 *     This is to be used while debugging and after entries in a new IAT Directory has been resolved.
 *
 * Author: TGZ
 * Version: 0.0.1
 * Date: 12 Apr 2019
 *
 * Sample hash: 304115CEF6CC7B81F4409178CD0BCEA2B22FD68CA18DFD5432C623CBBB507154
 *
 * Example:
 *     .data:10086C64 dword_10086C64 dd 75AB48C7h
 * will become:
 *     .data:10086C64 decrypted_kernel32_LoadLibraryA dd offset kernel32_LoadLibraryA
 * this will be done for:
 *     <every other variable in that new IAT Directory>
 *
 * Usage:
 *     Modify "current_address" and "end_address" to be the start and end virtual addresses of the new IAT Directory after the addresses have been resolved.
 *     If file was a DLL which we manually converted to an EXE, make sure to remove the "DLL can move" characteristics in Optional_header->DllCharacteristics from our PE parser so that ASLR is disabled, otherwise the offsets are going to change on each invocation
 *
 * Notes:
 *     We need to use get_name instead of get_func_name. This is because get_name works 100% of the time, but get_func_name does not work unless IDA has already seen that function in the disassembly (e.g. press "g" and go to that address so that it is recognized as a function).
 */

import idautils;

current_address = 0x10086C60;
end_address = 0x10086DD4;

while end_address > current_address:
  current_func_address = read_dbg_dword(current_address);
  function_name = get_name(current_func_address);
  if(function_name):
    print function_name + " " + hex(current_func_address);   
    set_name(current_address, "decrypted_"+function_name, flags=0);
  else:
    print "Failed: " + hex(current_func_address) + " " + function_name;
  current_address += 0x4;
