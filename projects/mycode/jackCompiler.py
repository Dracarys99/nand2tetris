import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",type=str,required=False,default="./",help="The path where the input files exist and output files need to be stored.")
args = parser.parse_args()
# print(args.path)
dir_files = os.listdir(args.path)
# print(dir_files)
files=[]
for f in dir_files:
    if(f.endswith(".jack")):
        files.append(f)
dir_files.clear()
# print(files)
if(len(files)==0):
    print("NO '.jack' FILES FOUND.")
    exit()
keywords=["class","constructor","function","method","field","static","var","int","char","boolean","void","true","false",
                "null","this","let","do","if","else","while","return"]
symbols=["{","}","(",")","[","]",".",",",";","+","-","*","/","&","|","<",">","=","~"]
allowedstart = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def classify(tok):
    if(tok in keywords):
        return "keyword"
    elif(tok in symbols):
        return "symbol"
    elif(tok.isdigit()):
        return "integerConstant"
    elif(tok.startswith('"')):
        return "stringConstant"
    elif any(tok.startswith(a) for a in allowedstart):
        return "identifier"
    else:
        print("ILLEGAL TOKEN CANDIDATE:"+tok)
        return "none"
def mysplit(d):
    l=0
    tmp=[]
    d=d.strip()
    for k in range(len(d)):
        if(d[k]!="\n"):
            if(d[l]!='"'):
                if(d[k]==" "):
                    if(d[l]!=" "):
                        tmp.append(d[l:k])
                    l=k+1
                elif(d[k] in symbols):
                    tmp.append(d[l:k])
                    tmp.append(d[k])
                    l=k+1
            elif(d[k]=='"') and l!=k:
                tmp.append(d[l:k])
                l=k+1
    k=[]
    l=0
    for t in tmp:
        if(len(t)==0):
            l=l+1
            k=t
    for i in range(l):
        tmp.remove(k)
    if(d!="\n"):
        return tmp
for file in files:
    infilename = file[:-5]
    # print(infilename)
    source = args.path+file
    destination_tokens = args.path+infilename+"T.xml"
    destination_parser = args.paht+infilename+".xml"
    skip=False
    with open(source,"r") as f:
        data = f.readlines()
        rd=[]
        data=[d.strip() for d in data]
        for d in data:
            if(not skip):
                k=d.find("//")
                if(k < 0):
                    l=d.find("/*")
                    if(l<0):
                        rd.append(d.strip())
                    elif(d.endswith("*/")):
                        skip=False
                    else:
                        skip=True
                        rd.append(d[:l].strip())                        
                elif(k>0):
                    rd.append(d[:k].strip())
            else:
                k=d.find("*/")
                if(k>=0):
                    tmp=d[k+2:]
                    if(len(tmp)>0):
                        rd.append(tmp)
                    skip=False
        data.clear()
        k=[]
        l=0
        for d in rd:
            if(len(d)==0):
                k=d
                l=l+1
        for i in range(l):
            rd.remove(k)
        # for d in rd:
        #     print(d)
        # print()
        tokens=["<tokens>"]
        for d in rd:
            tmp=mysplit(d)
            for tok in tmp:
                # if(tok.endswith(";")):
                #     c=classify(tok[:-1])
                #     tokens.append("<"+c+">"+tok[:-1]+"</"+c+">\n")
                #     tokens.append("<symbol>;</symbol>\n")
                # else:
                c=classify(tok)
                if(c=="stringConstant"):
                    tok=tok[1:]
                elif(tok=="<"):
                    tok="&lt;"
                elif(tok==">"):
                    tok="&gt;"
                elif(tok=="&"):
                    tok="&amp;"
                elif(tok=='"'):
                    tok="&quot;"
                tokens.append("<"+c+"> "+tok+" </"+c+">")
        tokens.append("</tokens>")
        with open(destination,"w") as wfile:
            for d in tokens:
                wfile.write(d+"\n")
        # for tok in tokens:
        #     print(tok)
        # print()