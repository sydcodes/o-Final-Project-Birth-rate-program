def encryption(s,n):
    A= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #etc
    enc = ""
    for c in s:
        if c == ' ':
            enc = enc + c
        else:
            i = A.index(c)
            #print(c,i,i+n,A[i+n])
            enc = enc+A[(i+n) % 26] #helps us stay within out list
            #print(c,i)
    return enc+str(n)#b/c string int

def decryption(W):
    decrypt = ""
    A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']      # etc
    n = ""
    for c in W:
        if c in ['0','1','2','3','4','5','6','7','8','9']:
            n += c
    n = int(n)

    for c in W:

        if c == ' ':
            decrypt = decrypt + c

    for i in range(len(W)):
        c = W[i]
        if c in A:
            indx = (A.index(c) - n) % 26
            decrypt = decrypt +A[indx]
    print(decrypt)

def main ():
    E=encryption("hello world",1)
    print(E)
    decryption(E)
    #W = encryption("hello world",1)
    #decryption(W)



main()