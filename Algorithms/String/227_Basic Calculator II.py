class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s="".join(s.split())
        if not s or len(s)==0:
            return "0"
        stack=[]
        num=0
        sign='+'
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+ord(s[i])-ord("0")
            #if (not s[i].isdigit() and not s[i].isspace()) or i==len(s)-1:
            if not s[i].isdigit() or i==len(s)-1:
                if sign=="+":
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack.append(stack.pop()*num)
                else:
                    tmp=stack.pop()
                    if tmp//num<0 and tmp%num!=0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                if i<len(s)-1:
                    sign=s[i]
                    num=0
        return sum(stack)