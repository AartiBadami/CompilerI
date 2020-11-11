This interpreter consumes simple arithmetic statements (see below for specific LL(1) grammar rules) and parses, tokenizes, and executes the statements line-by-line.  This means there are compile-time errors and all errors are caught at runtime.  The parser is implemented with recursive descent. (see repository for demo link)

--Grammar Rules--  
< Program >   ::= < StmtList >.
< StmtList >  ::= < Stmt > < NextStmt >
< NextStmt >  ::= ;< StmtList > | e
< Stmt >      ::= < Assign > | < Print >
< Assign >    ::= < Id > = < Expr >
< Print >     ::= !< Id >
< Expr >      ::= + < Expr > < Expr >
              | - < Expr > < Expr >
              | * < Expr > < Expr >
              | / < Expr > < Expr >
              | < Id >
              | < Const >
< Id >        ::= a | b |c
< Const >     ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  


--Examples--
Sample input #1:
a=3;b=2;c=+ab;!c
Sample output #1:
5

Sample input #2:
a=+12;!a.b
Sample output #2:
syntax error


--Running the Tests--
1) cd /path/to/CompilerI/directory
2) type command : "python interpreter1.py"
3) type input when prompted and then hit enter

Any output will be printed to the console.
Please note that the end of input is signified by '\n'.
