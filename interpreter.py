# map for variable lookup : map(key=variable, value=value)

import sys
next = None
src = ""
symtable = {}


def Program():
  global src
  scan()
  StmtList()
  if next != ".":
    error(1)
  else:
    scan()
    if next != "\n":
      error(1)
    # src = ""
    

def StmtList():
  if next == "a" or next == "b" or next == "c" or next == "!":
    Stmt()
  else:
    error(1)

  NextStmt()

def NextStmt():
  scan()
  if next == ";":
    scan()
    StmtList()
  else:
    return

def Stmt():
  if next == "a" or next == "b" or next == "c":
    Assign()
  elif next == "!":
    scan()
    Print()
  else:
    error(1)

def Assign():
  var_name = next
  scan()
  if next == "=":
    scan()
    value = Expr()
    symtable[var_name] = value
  else:
    error(1)

def Print():
  if next == "a" or next == "b" or next == "c":
    if next in symtable: print(symtable[next])
    else: error(2)
  else:
    error(1)

def Expr():
  if next == "+" or next == "-" or next == "*" or next == "/":
    op = next
    scan()
    value1 = Expr()
    scan()
    value2 = Expr()
    if type(value1) == "str":
      if value1 in symtable: value1 = symtable[value1]
      else: error(2)
    if type(value2) == "str":
      if value2 in symtable: value2 = symtable[value2]
      else: error(2)

    # operator calculations
    if op == "+": return (value1 + value2)
    elif op == "-": return (value1 - value2)
    elif op == "*": return (value1 * value2)
    else: # division op -- check for runtime error
      if value2 == 0: error(2)
      else: return (value1 / value2)

  elif next == "a" or next == "b" or next == "c": # id
    return Id()
  elif next.isdigit():
    return Const()
  else:
    error(1)

def Id():
  if next in symtable: return symtable[next]
  else: error(2)

def Const():
  return int(next)



def error(n):
  if n == 1:
    sys.stdout.write("syntax error\n")
    sys.exit(1)
  elif n == 2:
    sys.stdout.write("exception\n")
    sys.exit(1)
  else:
    sys.stdout.write("ERROR:%i, SOURCE:%s\n" % (n, src))
    sys.exit(1)

def getchar():
  c = sys.stdin.read(1)
  if len(c) > 0:
    return c
  else:
    return None

def scan():
  global next
  global src
  next = getchar()
  # src += next


def main():
  Program()


if __name__ == "__main__":
  main()







  
