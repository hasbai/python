#filename property.py
import os

def printfp():
  '''This function will check 
     and print the information
     of file 'sample.txt' '''
  fh = open('sample.txt')
  try:
    print('file name  : %s' % fh.name)
    print('access mode: %s' % fh.mode)
    print('encoding   : %s' % fh.encoding)
    print('closed     : %s' % fh.closed)
  finally:
    fh.close()
#end printfp

if __name__=='__main__':
  printfp()
#end if
