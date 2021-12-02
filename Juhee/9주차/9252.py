import sys

string1=sys.stdin.readline().strip().upper()  #옆 공백을 없애주어야함
string2=sys.stdin.readline().strip().upper()

len1=len(string1)
len2=len(string2)

# 9251과 다르게 최장 길이가 아닌 문자열
#원리는 같음
lcs_list=[[""]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if string1[i-1]==string2[j-1]:
            lcs_list[i][j]=lcs_list[i-1][j-1]+string1[i-1]
        else:
            if len(lcs_list[i-1][j])>=len(lcs_list[i][j-1]):
                lcs_list[i][j]=lcs_list[i-1][j]
            else:
                lcs_list[i][j]=lcs_list[i][j-1]

print(len(lcs_list[len1][len2]))
print(lcs_list[len1][len2])

#실행하면 결과 값 잘나오는데 백준에 넣으면 런타임에러