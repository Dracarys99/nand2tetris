//push constant 111
@111
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//push constant 333
@333
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//push constant 888
@888
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//pop static 8
@SP
MA=M-1
D=M
@StaticTest.8
M=D
//pop static 3
@SP
MA=M-1
D=M
@StaticTest.3
M=D
//pop static 1
@SP
MA=M-1
D=M
@StaticTest.1
M=D
//push static 3
@StaticTest.3
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
//push static 1
@StaticTest.1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
//sub
@SP
MA=M-1
D=M
@SP
MA=M-1
D=M-D
@SP
A=M
M=D
D=A+1
@SP
M=D
//push static 8
@StaticTest.8
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
//add
@SP
MA=M-1
D=M
@SP
MA=M-1
D=M+D
@SP
A=M
M=D
D=A+1
@SP
M=D
