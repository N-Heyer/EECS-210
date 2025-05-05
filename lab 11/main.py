'''
Name:Nick Heyer 
KUID:3142337
LAB Session:Thursday 4:30pm
LAB Assignment: 11
Description: program for converting an arithmetic expression in prefix form to its equivalent in postfix form
Collaborators: NONE
'''
#make sure token is an operator
def is_op(token):
    return token in '+-*/^'  #return True if token is a valid operator

#convert pre to post
def pre_to_post(tokens):
    stack = []  #stack that hold results

    #loop thru tokens in reverse 
    for token in reversed(tokens):
        if is_op(token):
            a = stack.pop()  #pop first operator
            b = stack.pop()  #pop second operator
            stack.append(f"{a} {b} {token}")  #combine to make post
        else:
            stack.append(token)  # if operator push to stack 

    return stack[0] #return stack w final results at top

#get user input / assume valid
expr = input("Enter prefix expression (space separated): ")

#split into indiv tokens
tokens = expr.split()

#convert and print postfix expr
print(pre_to_post(tokens)) 