import re
s = '12Nigel Sahl11_99'
resultNoInt = ''.join([i for i in s if not i.isdigit()])
result = ''.join([i for i in s if i.isalpha()])
def nospecial(text):
	text = re.sub("[^a-zA-Z012345678-9]+_", "",text)
	return text
print((s))
print(nospecial(s))
print((resultNoInt))
print((result))