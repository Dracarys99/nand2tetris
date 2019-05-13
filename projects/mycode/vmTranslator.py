import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",type=str,required=False,default="./",help="The path where the input file exists and output file needs to be stored(Optional)\nDefault= ./")
parser.add_argument("--input","-i",type=str,nargs="+",required=True,help="Input file name(Required)")
parser.add_argument("--output","-o",type=str,default="./output.asm",required=False,help="Output file name(Optional)\nDefault name = output.hack")
args=parser.parse_args()
destination = args.path+args.output

def pushfun(ins,i):
    if(ins[1].lower()=="constant"):
        d = "@"+str(ins[2])+"\nD=A\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    elif(ins[1].lower()=="argument"):
        d = "@"+str(ins[2])+"\nD=A\n@ARG\nA=M+D\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    elif(ins[1].lower()=="local"):
        d = "@"+str(ins[2])+"\nD=A\n@LCL\nA=M+D\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    elif(ins[1].lower()=="this"):
        d = "@"+str(ins[2])+"\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    elif(ins[1].lower()=="that"):
        d = "@"+str(ins[2])+"\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    elif(ins[1].lower()=="pointer"):
        # print(str(i)+":WARNING:Pushing the value of 'pointer 0' and 'pointer 1' is not advisable.")
        if(ins[2]=="0"):
            d = "@THIS\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
        elif(ins[2]=="1"):
            d = "@THAT\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    elif(ins[1].lower()=="temp"):
        k=int(ins[2])
        if(k>=0) and k<8:
            d = "@R"+str(k+5)+"\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
        else:
            print(str(i)+":ERROR:Offset Value with Temp Segment out of range.")
    elif(ins[1].lower()=="static"):
        d = "@"+infilename+str(ins[2])+"\nD=M\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    # print(d)
    return d
def popfun(ins,i):
    if(ins[1].lower()=="constant"):
        print(str(i)+":ERROR:Popping the value to an address in the constant segment is not allowed.")
        # d = "@SP\nMA=M-1\nD=M\n@"+str(ins[2])+"\nM=D"
    elif(ins[1].lower()=="argument"):
        d = "@"+str(ins[2])+"\nD=A\n@ARG\nD=M+D\n@R13\nM=D\n@SP\nMA=M-1\nD=M\n@R13\nA=M\nM=D\n"
    elif(ins[1].lower()=="local"):
        d = "@"+str(ins[2])+"\nD=A\n@LCL\nD=M+D\n@R13\nM=D\n@SP\nMA=M-1\nD=M\n@R13\nA=M\nM=D\n"
    elif(ins[1].lower()=="this"):
        d = "@"+str(ins[2])+"\nD=A\n@THIS\nD=M+D\n@R13\nM=D\n@SP\nMA=M-1\nD=M\n@R13\nA=M\nM=D\n"
    elif(ins[1].lower()=="that"):
        d = "@"+str(ins[2])+"\nD=A\n@THAT\nD=M+D\n@R13\nM=D\n@SP\nMA=M-1\nD=M\n@R13\nA=M\nM=D\n"
    elif(ins[1].lower()=="pointer"):
        if(ins[2]=="0"):
            d = "@SP\nMA=M-1\nD=M\n@THIS\nM=D\n"
        elif(ins[2]=="1"):
            d = "@SP\nMA=M-1\nD=M\n@THAT\nM=D\n"
    elif(ins[1].lower()=="temp"):
        k=int(ins[2])
        if(k>=0) and k<8:
            d = "@SP\nMA=M-1\nD=M\n@R"+str(k+5)+"\nM=D\n"
        else:
            print(str(i)+":ERROR:Offset Value with Temp Segment out of range.")
    elif(ins[1].lower()=="static"):
        d = "@SP\nMA=M-1\nD=M\n@"+infilename+str(ins[2])+"\nM=D\n"
    return d
def addfun(ins,i):
    # return "@2\nD=A\n@SP\nMA=M-D\nD=M\nA=A+1\nA=M\nD=D+A\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M+D\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def subfun(ins,i):
    # return "@2\nD=A\n@SP\nMA=M-D\nD=M\nA=A+1\nA=M\nD=D-A\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M-D\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def negfun(ins,i):
    return "@SP\nA=M-1\nD=-M\n@SP\nA=M-1\nM=D\n"
def andfun(ins,i):
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M&D\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def orfun(ins,i):
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M|D\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def notfun(ins,i):
    return "@SP\nA=M-1\nD=!M\n@SP\nA=M-1\nM=D\n"
def eqfun(ins,i):
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M-D\n@"+str(i)+"_cond_true\nD;JEQ\nD=0\n@"+str(i)+"_cond_update\n0;JMP\n("+str(i)+"_cond_true)\nD=0\nD=!D\n("+str(i)+"_cond_update)\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def ltfun(ins,i):
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M-D\n@"+str(i)+"_cond_true\nD;JLT\nD=0\n@"+str(i)+"_cond_update\n0;JMP\n("+str(i)+"_cond_true)\nD=0\nD=!D\n("+str(i)+"_cond_update)\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def gtfun(ins,i):
    return "@SP\nMA=M-1\nD=M\n@SP\nMA=M-1\nD=M-D\n@"+str(i)+"_cond_true\nD;JGT\nD=0\n@"+str(i)+"_cond_update\n0;JMP\n("+str(i)+"_cond_true)\nD=0\nD=!D\n("+str(i)+"_cond_update)\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
def labelfun(ins,i):
    return "("+str(ins[1])+")\n"
def ifGotofun(ins,i):
    return "@SP\nMA=M-1\nD=M\n@"+str(ins[1])+"\nD;JNE\n"
def gotofun(ins,i):
    return "@"+str(ins[1])+"\n0;JMP\n"
def callfun(ins,i):
    d="@retlabel_"+str(i)+"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n" #Push return address
    d=d+"@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    d=d+"@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    d=d+"@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    d=d+"@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
    d=d+"@"+str(int(ins[2])+5)+"\nD=A\n@SP\nD=M-D\n@ARG\nM=D\n"
    d=d+"@SP\nD=M\n@LCL\nM=D\n"
    d=d+"@"+str(ins[1])+"\n0;JMP\n"
    d=d+"(retlabel_"+str(i)+")\n"
    return d
def retfun(ins,i):
    d="@LCL\nD=M\n@R13\nM=D\n"
    d=d+"@5\nA=D-A\nD=M\n@R14\nM=D\n"
    d=d+"@SP\nMA=M-1\nD=M\n@ARG\nA=M\nM=D\n"
    d=d+"@1\nD=A\n@ARG\nD=M+D\n@SP\nM=D\n"
    d=d+"@1\nD=A\n@R13\nD=M-D\nA=D\nD=M\n@THAT\nM=D\n"
    d=d+"@2\nD=A\n@R13\nD=M-D\nA=D\nD=M\n@THIS\nM=D\n"
    d=d+"@3\nD=A\n@R13\nD=M-D\nA=D\nD=M\n@ARG\nM=D\n"
    d=d+"@4\nD=A\n@R13\nD=M-D\nA=D\nD=M\n@LCL\nM=D\n"
    d=d+"@R14\nA=M\n0;JMP\n"
    return d
def functionfun(ins,i):
    d="("+str(ins[1])+")\n"
    for i in range(int(ins[2])):
        d=d+"@0\nD=A\n@SP\nA=M\nM=D\nD=A+1\n@SP\nM=D\n"
    return d
funcDict={
    "push":pushfun,
    "pop":popfun,
    "add":addfun,
    "sub":subfun,
    "neg":negfun,
    "and":andfun,
    "or":orfun,
    "not":notfun,
    "lt":ltfun,
    "gt":gtfun,
    "eq":eqfun,
    "label":labelfun,
    "if-goto":ifGotofun,
    "goto":gotofun,
    "call":callfun,
    "return":retfun,
    "function":functionfun
}
assemblyCode=[]
for file in args.input:
    infilename = file[:-2]
    #print(infilename)
    source = args.path+file
    with open(source,"r") as f:
        data = f.readlines()
        rd=[]
        data=[d.strip() for d in data]
        for d in data:
            k=d.find("//")
            if(k < 0):
                rd.append(d.strip())
            elif(k>0):
                rd.append(d[:k].strip())
        data.clear()
        k=[]
        l=0
        for d in rd:
            if(len(d)==0):
                k=d
                l=l+1
        for i in range(l):
            rd.remove(k)
    # print(rd)
    for d in rd:
        data.append(d.split(" "))
    # print(data)
    
    for i in range(len(data)):
        ins=data[i]
        assemblyCode.append("//"+rd[i]+"\n")
        assemblyCode.append(funcDict[ins[0].lower()](ins,i))
        i=i+1
    # for line in assemblyCode:
    #     print(line)
    #     print()

with open(destination,"w") as wfile:
    for d in assemblyCode:
        wfile.write(d)
