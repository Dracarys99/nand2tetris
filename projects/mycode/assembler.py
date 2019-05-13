from numpy import binary_repr
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",type=str,required=False,default="./",help="The path where the input file exists and output file needs to be stored(Optional)\nDefault= ./")
parser.add_argument("--input","-i",type=str,required=True,help="Input file name(Required)")
parser.add_argument("--output","-o",type=str,default="./output.asm",required=False,help="Output file name(Optional)\nDefault name = output.hack")
args=parser.parse_args()
# infilename = args.input[:-2]
#print(infilename)
source = args.path+args.input
destination = args.path+args.output
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
    k=[]
    l=0
    for d in rd:
        if(len(d)==0):
            k=d
            l=l+1
    for i in range(l):
        rd.remove(k)
    # print(rd)
    data.clear()

# with open(write,"w") as wfile:
#     for d in rd:
#         wfile.write(d+"\n")
k=0
labelsAndVariables = {"SCREEN":"100000000000000","KBD":"110000000000000"}
labelsAndVariables["SP"]=binary_repr(0,15)
labelsAndVariables["LCL"]=binary_repr(1,15)
labelsAndVariables["ARG"]=binary_repr(2,15)
labelsAndVariables["THIS"]=binary_repr(3,15)
labelsAndVariables["THAT"]=binary_repr(4,15)
for i in range(0,16):
    labelsAndVariables["R"+str(i)]=binary_repr(i,15)
compute = {
    "0":"0101010",
    "1":"0111111",
    "-1":"0111010",
    "D":"0001100",
    "A":"0110000",
    "!D":"0001101",
    "!A":"0110001",
    "-D":"0001111",
    "-A":"0110011",
    "D+1":"0011111",
    "1+D":"0011111",
    "A+1":"0110111",
    "1+A":"0110111",
    "D-1":"0001110",
    "-1+D":"0001110",
    "A-1":"0110010",
    "-1+A":"0110010",
    "D+A":"0000010",
    "A+D":"0000010",
    "D-A":"0010011",
    "-A+D":"0010011",
    "A-D":"0000111",
    "-D+A":"0000111",
    "D&A":"0000000",
    "A&D":"0000000",
    "D|A":"0010101",
    "A|D":"0010101",
    "M":"1110000",
    "!M":"1110001",
    "-M":"1110011",
    "M+1":"1110111",
    "1+M":"1110111",
    "M-1":"1110010",
    "-1+M":"1110010",
    "D+M":"1000010",
    "M+D":"1000010",
    "D-M":"1010011",
    "-M+D":"1010011",
    "M-D":"1000111",
    "-D+M":"1000111",
    "D&M":"1000000",
    "M&D":"1000000",
    "D|M":"1010101",
    "M|D":"1010101"
}
dest={
    "default":"000",
    "M":"001",
    "D":"010",
    "MD":"011",
    "DM":"011",
    "A":"100",
    "AM":"101",
    "MA":"101",
    "AD":"110",
    "DA":"110",
    "AMD":"111",
    "MAD":"111",
    "ADM":"111",
    "DMA":"111",
    "DAM":"111",
    "MDA":"111"
}
jump={
    "default":"000",
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011",
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111"
}
for d in rd:
    if(d.startswith("(")):
        labelsAndVariables[d[1:d.find(")")]] = binary_repr(k,15)
    elif(d.startswith("@")):
        # print("@")
        # print(d[1:])
        # print(not d[1:].isdigit())
        # print(labelsAndVariables.get(d[1:])!=None)
        if(not d[1:].isdigit() and labelsAndVariables.get(d[1:])==None):
            labelsAndVariables[d[1:]]=None
        k=k+1
    else:
        k=k+1
k=16
for i in labelsAndVariables:
   if(labelsAndVariables[i]==None):
       labelsAndVariables[i]=binary_repr(k,15)
       k=k+1 
# print(labelsAndVariables)
macCode=[]
for d in rd:
    if(not d.startswith("(")):
        # print(d)
        if(d.startswith("@")):
            if(not d[1:].isdigit()):
                l="0"+labelsAndVariables[d[1:]]
            else:
                l="0"+binary_repr(int(d[1:]),15)
            # print(l)
            macCode.append(l)
        else:
            l="111"
            k=d.find(";")
            if(k==-1):
                l=l+compute[d[d.find("=")+1:]]+dest[d[:d.find("=")].upper()]+jump["default"]
            else:
                l=l+compute[d[:k]]+dest["default"]+jump[d[k+1:]]
            macCode.append(l)
# print(macCode)

with open(destination,"w") as wfile:
    for d in macCode:
        wfile.write(d+"\n")
