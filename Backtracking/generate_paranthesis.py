def gen_paran(ob,cb,n,s=[]):
    
    if cb==n:
        print (s)
        return
    
    else:
        if ob>cb:
            s.append(')')
            gen_paran(ob,cb+1,n,s)
            s.pop()
    
        if ob<n:
            s.append('(')
            gen_paran(ob+1,cb,n,s)
            s.pop()
    
    return

print(gen_paran(0,0,3))