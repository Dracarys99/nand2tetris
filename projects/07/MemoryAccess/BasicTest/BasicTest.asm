//push constant 10
@10
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//pop local 0
@0
D=A
@LCL
D=M+D
@R13
M=D
@SP
MA=M-1
D=M
@R13
A=M
M=D
//push constant 21
@21
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//push constant 22
@22
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//pop argument 2
@2
D=A
@ARG
D=M+D
@R13
M=D
@SP
MA=M-1
D=M
@R13
A=M
M=D
//pop argument 1
@1
D=A
@ARG
D=M+D
@R13
M=D
@SP
MA=M-1
D=M
@R13
A=M
M=D
//push constant 36
@36
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//pop this 6
@6
D=A
@THIS
D=M+D
@R13
M=D
@SP
MA=M-1
D=M
@R13
A=M
M=D
//push constant 42
@42
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//push constant 45
@45
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//pop that 5
@5
D=A
@THAT
D=M+D
@R13
M=D
@SP
MA=M-1
D=M
@R13
A=M
M=D
//pop that 2
@2
D=A
@THAT
D=M+D
@R13
M=D
@SP
MA=M-1
D=M
@R13
A=M
M=D
//push constant 510
@510
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//pop temp 6
@SP
MA=M-1
D=M
@R11
M=D
//push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
//push that 5
@5
D=A
@THAT
A=M+D
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
//push argument 1
@1
D=A
@ARG
A=M+D
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
//push this 6
@6
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
//push this 6
@6
D=A
@THIS
A=M+D
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
//push temp 6
@R11
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
