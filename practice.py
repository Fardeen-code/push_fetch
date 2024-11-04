def values(str):
    coun=0
    val=0
    for i in str:
        val+=(ord(i)-ord('A')+1)+coun*(ord('Z')-ord('A')+1)-coun
        coun+=1
    return val
str=input()
print(values(str))