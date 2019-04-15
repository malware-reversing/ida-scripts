```
unit42_execution_coloring.py.py
Description:
    Colors the execution path of the file (this executes the file and lets it fully run via debugger)
    No color = not executed
    Blue color = 4 shades of blue, gets darker as it gets executed repeatedly
Author: Unit 42
Reference: https://unit42.paloaltonetworks.com/using-idapython-to-make-your-life-easier-part-4/
'''

heads = Heads(SegStart(ScreenEA()), SegEnd(ScreenEA()))
for i in heads:
	SetColor(i, CIC_ITEM, 0xFFFFFF)
 
def get_new_color(current_color):
	colors = [0xffe699, 0xffcc33, 0xe6ac00, 0xb38600]
	if current_color == 0xFFFFFF:
		return colors[0]
	if current_color in colors:
		pos = colors.index(current_color)
		if pos == len(colors)-1:
			return colors[pos]
		else:
			return colors[pos+1]
	return 0xFFFFFF
 
RunTo(BeginEA())
event = GetDebuggerEvent(WFNE_SUSP, -1)
 
EnableTracing(TRACE_STEP, 1)
event = GetDebuggerEvent(WFNE_ANY|WFNE_CONT, -1)
while True:
	event = GetDebuggerEvent(WFNE_ANY, -1)
	addr = GetEventEa()
	current_color = GetColor(addr, CIC_ITEM)
	new_color = get_new_color(current_color)
	SetColor(addr, CIC_ITEM, new_color)
	if event <= 1: break
