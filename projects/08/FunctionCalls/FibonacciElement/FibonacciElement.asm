//function Sys.init 0
(Sys.init)
//push constant 4
@4
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//call Main.fibonacci 1
@retlabel_2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(retlabel_2)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP
//function Main.fibonacci 0
(Main.fibonacci)
//push argument 0
@0
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
//push constant 2
@2
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
//lt
@SP
MA=M-1
D=M
@SP
MA=M-1
D=M-D
@8_cond_true
D;JLT
D=0
@8_cond_update
0;JMP
(8_cond_true)
D=0
D=!D
(8_cond_update)
@SP
A=M
M=D
D=A+1
@SP
M=D
//if-goto IF_TRUE
@SP
MA=M-1
D=M
@IF_TRUE
D;JNE
//goto IF_FALSE
@IF_FALSE
0;JMP
//label IF_TRUE
(IF_TRUE)
//push argument 0
@0
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
//return
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
MA=M-1
D=M
@ARG
A=M
M=D
@1
D=A
@ARG
D=M+D
@SP
M=D
@1
D=A
@R13
D=M-D
A=D
D=M
@THAT
M=D
@2
D=A
@R13
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@R13
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@R13
D=M-D
A=D
D=M
@LCL
M=D
@R14
A=M
0;JMP
//label IF_FALSE
(IF_FALSE)
//push argument 0
@0
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
//push constant 2
@2
D=A
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
//call Main.fibonacci 1
@retlabel_18
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(retlabel_18)
//push argument 0
@0
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
//push constant 1
@1
D=A
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
//call Main.fibonacci 1
@retlabel_22
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(retlabel_22)
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
//return
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
MA=M-1
D=M
@ARG
A=M
M=D
@1
D=A
@ARG
D=M+D
@SP
M=D
@1
D=A
@R13
D=M-D
A=D
D=M
@THAT
M=D
@2
D=A
@R13
D=M-D
A=D
D=M
@THIS
M=D
@3
D=A
@R13
D=M-D
A=D
D=M
@ARG
M=D
@4
D=A
@R13
D=M-D
A=D
D=M
@LCL
M=D
@R14
A=M
0;JMP
