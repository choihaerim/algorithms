def solution(n, words):
    answer = [0,0]
    turn=1
    before=words[0][-1]
    for i in range(1,len(words)):
        if words[i][0]!=before or words[i] in words[:i]:
            #탈락자 발생
            a,b=divmod(i,n)
            answer[1]=a+1
            answer[0]=b+1
            break
        else:
            before=words[i][-1]
        
    return answer