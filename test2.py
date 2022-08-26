import sys

for idx, item in enumerate(sys.argv):
    if idx == 0:
        print(f'File {item}')
    else:
        print(f'Arg{idx} > {item}')
        
