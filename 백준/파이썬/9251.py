n = list(str(input()))

m = list(str(input()))



lcs_list =[[0 for _ in range(len(n) + 1)] for _ in range(len(m) + 1)]

answer = 0



for i in range(len(n)):

    for j in range(len(m)):

        if n[i] ==m[j]:

            lcs_list[j+1][i+1] = lcs_list[j][i] + 1

        else:

            lcs_list[j+1][i+1] = max(lcs_list[j][i+1],lcs_list[j+1][i])



print(lcs_list[-1][-1])