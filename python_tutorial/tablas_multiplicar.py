for i in range(0,6,1):
  if i != 0:
    print('La tabla del', i)
    for j in range(0,10,1):
      print(i*(j+1), end=' ')
    print('\n'*2)