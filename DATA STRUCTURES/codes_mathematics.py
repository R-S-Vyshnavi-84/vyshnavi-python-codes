'''
OPERATORS=set(['+','-' ,'*','/','(',')','^'])
PRIORITY={'+':1, '-':1, '*':2 ,'/':2, '^':3}

def infix_to_postfix(expression):
    stack=[]
    output=''
    for ch in expression:
        if ch not in OPERATORS:
            output+=ch
        elif ch=="(":                                # else operators should be in stack
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
expression=input('Enter infix expression: ')
print('infix expression: ',expression)
print('postfix expression: ',infix_to_postfix(expression))
'''
def postfixevaluation(s):
    st=[]
    s=s.split()
    print(s)
    print(len(s))
    for i in range(len(s)):
        if s[i].isdigit():
            st.append(int(s[i]))
        elif s[i]=='+':
            a=st.pop()
            b=st.pop()
            st.append(b+a)
        elif s[i]=='-':
            a=st.pop()
            b=st.pop()
            st.append(b-a)
        elif s[i]=='*':
            a=st.pop()
            b=st.pop()
            st.append(b*a)
        elif s[i]=='/':
            a=st.pop()
            b=st.pop()
            st.append(b/a)
        elif s[i]=='^':
            a=st.pop()
            b=st.pop()
            st.append(b^a)
    return st.pop()
s='10 2 8 * + 3 -'
val=postfixevaluation(s)
print(val)