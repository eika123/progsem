import sys

# modul readline virker ikke på windows...
if sys.platform != 'win32':
    import readline

print('running input_readline program')
for arg in sys.argv[1:]:
    print(arg)


a = 5
b = 2
c = 3