#!/usr/bin/python
def fortran_format_parser(format, string):
    res = []
    str_pos = 0
    #lets get rid of the ()
    format = format[1:-1]
    
    #each section is seperated by a comma
    sections = format.split(",")
    for x in range(len(sections)):
        sections[x] = sections[x].strip()
        rep = ""
        sec = sections[x]
        op = ""
        w = ""
        n = ""
        e = ""
        i = 0
        ch = sec[i]
        while ch in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            rep = rep + ch
            i += 1
            ch = sec[i]
        
        if ch in ("I", "F", "E", "A", "L", "X", "/", "T", "D"):
            op = ch
        else:
            raise Exception("No operator in section " + str(x))
        i += 1
        if(i < len(sec)):
            ch = sec[i]
            if op == "T":
                if ch in ("L", "R"):
                    op = op + ch
                    if(i < len(sec)): 
                        i += 1
                        ch = sec[i]
            
            while ch in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"):
                w = w + ch
                i += 1
                if i >= len(sec): break
                ch = sec[i]
            
            if ch == ".":
                i += 1
                ch = sec[i]
                while ch in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    n = n + ch
                    i += 1
                    if i >= len(sec): break
                    ch = sec[i]
                if ch == "E":
                    i += 1
                    ch = sec[i]
                    while ch in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        n = n + ch
                        i += 1
                        if i >= len(sec): break
                        ch = sec[i]
                    
        # rep = len(rep) if int(rep) else 1
        # w = len(w) > 0 if int(w) else 1
        # n = len(n) > 0 if int(n) else 1

        if len(rep):
            rep = int(rep)
        else:
            rep = 1 

        if len(w):
            w = int(w)
        else:
            w = 1 

        if len(n):
            n = int(n)
        else:
            n = 0
            
        if len(e):
             e = int(e)
        else:
             e = 2
        print rep, op, w, n, e
        
        for i in range(rep):
            sec = string[str_pos:str_pos+w]
            if op == "A":
                res.append(sec)
            elif op == "I":
                res.append(int(sec))
            elif op in ("D", "E", "F"):
                res.append(float(sec))
            elif op == "L":
                res.append(sec[-1]=="T") 
            str_pos += w
    return res
print fortran_format_parser("(I2,L2, X, F4.3, D9.3)", "44 T 1.420.111E+44")