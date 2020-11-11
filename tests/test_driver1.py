import os

# file to create, run, and execute test cases
tests = [("a=9.a\n", "syntax error"), ("a=0;!a.b\n", "0\nsyntax error"), ("a=0;!a.!\n", "0\nsyntax error"),
("a=3;b=2;c=+ab;!c.\n", "5"), ("a=4;c=2;b=+ac;!b.\n", "6"), ("a=4;!a.\n", "4"), ("a=4;!a\n", "4\nsyntax error"),
("a=6;;\n", "syntax error"), ("b=7;b.\n", "syntax error"),("c=9;b=9;a=*cb;!a.\n", "81"),("a=1;b=2;c=-ab;!c.\n", "-1"),
("a=1;b=2;c=/ab;!c.\n", "0"), ("a=b;b=4;.\n", "runtime error"), ("a=4;b=0;c=/ab;!c.\n", "runtime error"),
("a\n", "syntax error"), (".\n", "syntax error"), ("9\n", "syntax error"), ("a.\n", "syntax error"),
("0.\n", "syntax error"), ("0;a=b;0.\n", "syntax error"), ("a=1;b=4;/ba;!a.\n", "syntax error"), ("a=9;!a.\n", "9"), ("a=9;b=0;c=/ab;!c.\n", "runtime error"), ("a=9;b=3;c=/ab;a=/cb;!a.\n", "1"),
("a=4;b=1;c=*/+-ababa;!c.\n", "28"), ("a=1;b=1;c=/a*aa;!b.\n", "1"), ("a=1;b=2;b=/a*aa;!b.\n", "1"), 
("a=1;!a;!b.\n", "1\nruntime error"), ("a=1;!a;b=+aa;!b;c=*ab;!c;a=0;!a.\n", "1\n2\n2\n0"),
("a=1;!a;b=+aa;!b;!c;a=0;!a.\n", "1\n2\nruntime error")]

def make_tests():
  for i in range(len(tests)):
    test_name = "./tests/test" + str(i).zfill(2) + ".txt"
    sol_name = "./tests/sol" + str(i).zfill(2) + ".txt"
    f1 = open(test_name, "w")
    f2 = open(sol_name, "w")
    f1.write(tests[i][0])
    f2.write(tests[i][1])

    f1.close()
    f2.close()

def run_tests():
  num_total = len(tests)
  num_passed = len(tests)
  # runs each test case and saves the output in a file
  for i in range(len(tests)):
    output_name = "./tests/output" + str(i).zfill(2) + ".txt"
    test_name = "./tests/test" + str(i).zfill(2) + ".txt"
    f = open(output_name, "w")
    os.system(("python interpreter1.py < " + test_name + " > " + output_name))
    f.close()

    # compares output against actual solution and reports any discrepancies
    sol_name = "./tests/sol" + str(i).zfill(2) + ".txt"
    if not isSame(sol_name, output_name):
      num_passed -= 1
      print "input : ", tests[i]
      print("Expected Output : ")
      fsol = open(sol_name, "r")
      for line in fsol:
        print(line)
      fsol.close()

      print("Recieved Output : ")
      foutput = open(output_name, "r")
      for line in foutput:
        print(line)
      foutput.close()

  print num_passed, "/", num_total, " test cases passed"


def isSame(file1, file2):
  f1 = open(file1, "r")
  f2 = open(file2, "r")
  list1 = f1.readlines()
  list2 = f2.readlines()
  list2[-1] = list2[-1][:-1]
  f1.close()
  f2.close()

  if len(list1) != len(list2):
    return False

  for i in range(len(list1)):
    if list1[i] != list2[i]: return False
  return True


def main():
  make_tests()
  run_tests()

if __name__ == "__main__":
  main()
