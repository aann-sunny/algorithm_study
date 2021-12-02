import sys

string1=sys.stdin.readline().strip().upper()  #옆 공백을 없애주어야함
string2=sys.stdin.readline().strip().upper()

len1=len(string1)
len2=len(string2)

lcs_list=[[0]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if string1[i-1]==string2[j-1]:  #같은 문자열이라면
            lcs_list[i][j]=lcs_list[i-1][j-1]+1  #경우의 수 하나 더함
        else:
            lcs_list[i][j]=max(lcs_list[i-1][j],lcs_list[i][j-1])


print(lcs_list[len1][len2])
