# Related Problems
```diff
- leetcode 224. Basic Calculator  
- lintcode 227. Basic Calculator II
- leetocde 772. Basic Calculator III 
```
## prefix notation
	f(x,y,z)
	add(sub(8,div(5,2)),1)
	+ - 8/6 2 1
	
## Infix notation
	8-6/2+1
	
##postfix notation
	8 6 2 / - 1 +
	
    opperator stack: ======>
	 (-) (/) +
	 
postfix list: 8 6 2 / -

## infix to postfix conversion:
	
    If the current item is an operand, add it to the postfix list.
    If the current item is '(': append it to the operator stack
    If the current item is ')': 
	(a) Pop each operator from operator stack and append to postfix list until a lfet parenthesis is encountered
        (b) Remove the left parenthesis in the operator stack
    If the current item is an operator,:
    	(a) Pop operator from stack and add to postfix list which has the same or higher precedence than it
	(b) Append it to the operator stack
		
				
    2 * (8 - (4 -2) * 3) / 2
	
    operator stack========>
    * ( - ( -
	
## Basic CalculatorII

### Method 
Stack
```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=''.join(s.split())
        if not s or len(s)==0:
            return 0
        stack=[]
        num=0
        sign='+'
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            if not s[i].isdigit() or i==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack[-1]=stack[-1]*num
                else:
                    stack[-1]=int(stack[-1]/float(num))
                sign=s[i]
                num=0
        return sum(stack)
```
## Basic Calculator III

### Method 
Recursion  


```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        num=0
        sign='+'
        i=0
        while i<len(s):
            c=s[i]
            if c.isdigit():
                num=num*10+int(c)
            if c=='(':
                left=1
                j=i+1
                while left>0:
                    if s[j]=='(':
                        left+=1
                    elif s[j]==')':
                        left-=1
                    j+=1
                num=self.calculate(s[i+1:j-1])
                i=j-1
            if i==len(s)-1 or (c=='+' or c=='-' or c=='*' or c=='/'):
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack[-1]=stack[-1]*num
                elif sign=='/':
                    stack[-1]=int(stack[-1]/float(num))
                sign=c
                num=0
            print(stack)
            i+=1
        return sum(stack)
        
```

## Basic Calculator

### Method 
Stack+Postfix
  
```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        postfix=self.infix_To_postfix(s)
        print(postfix)
        operator={'+','-','*','/'}
        res=0
        stack=[]
        for i in range(len(postfix)):
            if postfix[i] not in operator:
                stack.append(postfix[i])
            else:
                num2=stack.pop()
                num1=stack.pop()
                if postfix[i]=='+':
                    stack.append(num1+num2)
                elif postfix[i]=='-':
                    stack.append(num1-num2)
                elif postfix[i]=='*':
                    stack.append(num1*num2)
                elif postfix[i]=='/':
                    stack.append(int(num1*1.0/num2))
        return stack[-1]
    
    
    def infix_To_postfix(self,s):
        precedence = {'+':1, '-':1, '*':2, '/':2} 
        postfix=[]
        operator=[]
        num=0
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
                if i==len(s)-1 or not s[i+1].isdigit():
                    postfix.append(num)
                    num=0
            if s[i]=='(':
                operator.append(s[i])
            if s[i]==')':
                while operator[-1]!='(':
                    postfix.append(operator.pop())
                operator.pop()
            if s[i] in precedence:
                if not operator or operator[-1] not in precedence:
                    operator.append(s[i])
                elif  precedence[s[i]]>precedence[operator[-1]]:
                    operator.append(s[i])
                else:
                    while operator and (operator[-1] in precedence and precedence[s[i]]<=precedence[operator[-1]]):
                        postfix.append(operator.pop())
                    operator.append(s[i])
        while operator:
            postfix.append(operator.pop())
        return (postfix)

```




                    right-=1