hexlist='303fff0 303fff1 303fff2 303fff3 3032f80 3034f80 3033f80'
hexlist='3031f84 303fffb 3032f84 3034f84'
hexread=[f'0x{i}' for i in hexlist.split()]
print(hexread)
hexread=[int(i,base=16) for i in hexread]
print(hexread)
hexread.sort()
print(hexread)
