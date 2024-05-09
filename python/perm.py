"""str="EAT"
def permute(s,e,n):
    swap(n[s],n[e])
    print(n)
permute(0,2,str)"""
def get_permutation(string, i=0):
 
    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('EAT'))
