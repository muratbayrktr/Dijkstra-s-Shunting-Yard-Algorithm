# TODO 1 : write the operand check function
# TODO 2 : write the parenthesis handling function
# TODO 3 : write the operator check function
# TODO 4 : write the operator precedence check function
# ------------------------------------------------------
# Yazar/Author : Murat Bayraktar
# Tarih/Date   : 2020-12-5
# 
# Tanım        : 
# Dijkstra'nın Shunting Yard algoritmasının programa 
# dökülmüş halidir. Infix bir ifadeyi alarak ifadedeki
# işlem önceliği karakter/işlem sınıflandırmasına dikkat
# ederek ve sağdan-soldan işlenmeli olduğuna dikkat ederek
# onu stack mantığını kullanarak postfix ifadeye dönüştürüyor.
# sleep fonksiyonu da adımların daha iyi gözükebilmesi amacıyla
# kullanılmıştır.
# 
# Description : 
# Implementation of Dijkstra's Shunting 
# yard algorithm. Programme takes an infix expression 
# and turns it into postfix expression. It shows every 
# step clearly for better comprehension.
#
# Parametreler/Parameters : stack,inital_expression,output_queue
# Örnek / Example :
#           infix = "A-B^C^D*(E-(F-G-H))/K"
#         postfix = "ABCD^^EFG-H--*K/-"
# ------------------------------------------------------
""" 
----------------------- PSEUDOCODE ----------------------
Get next token t from the input queue
if t is an operand then
    Add t to the output queue
if t is an operator then
    while There is an operator τ at the top of the stack, and either t is leftassociative
    and its precedence is less than or equal to the precedence of τ ,
    or t is right-associative and its precedence is less than the precedence of τ do
        Pop τ from the stack, to the output queue.
    Push t on the stack.
if t is a left parenthesis then
    Push t on the stack.
if t is a right parenthesis then
    Pop the operators from the stack, to the output queue until the top of the stack
    is a left parenthesis.
    Pop the left parenthesis.
if No more tokens to get then
    Pop the operators on the stack, if any, to the output queue.
----------------------- PSEUDOCODE ----------------------
Source: "Introduction to Programming Concepts with Case Studies in Python" , Göktürk Üçoluk-Sinan Kalkan, Chapter 3, Page: 84
"""

# example infix operation : A*(B+C)-D
# ORDER of arithmetic operations :
# 1. exponent ** right to left
# 2. multiplication * left to right
# 3. division / left to right
# 4. plus minus + - left to right

# operator dict according to precedence
operator_dict = {"^": 3,
                 "*": 2,
                 "/": 2,
                 "+": 1,
                 "-": 1,
                 #"(": 0,
                 #")": 8
                 }
# unnecesarry but might help for further arrangements
parenthesis_dict = {
                "(":1,
                ")":0
}
# operator associativity; left : 0, right: 1
operator_assoc = {"^": 1, # right
                  "*": 0, # left
                  "/": 0,
                  "+": 0,
                  "-": 0,
                  "(": 0,
                  ")": 0,
                  }
# import time for slowing the demonstration of steps
from time import sleep
import sys

# test cases are made without spaces 
# however if we like to include cases with spaces
# then we might need to add extre function in order to 
# arrange the initial expression to meet our needs.

if len(sys.argv) != 2:
    sys.exit('usage: ./dijsktras_shunting_yard.py <infix_expression>')

#test1 = "A*B+C-D"
#test2 = "A-B*(C-D-E)/F-G"
#test3 = "A-B^C^D*(E-(F-G-H))/K"
#test4 = "A^B-C/(D-E+(F*G^H))-L+M*N"

initial_expression = sys.argv[1].strip()
stack = []
output_queu = []

# if it is an operand we push it to the output queu
def operand_check(element):
    if (element not in operator_dict.keys()) and (element not in parenthesis_dict.keys()):
        output_queu.append(element)


def parenthesis_check(element):
    # push down the left parenthesis
    if element == "(":
        stack.append(element)
    # if it's right parenthesis then pop everything out of stack until
    # you reach left parenthesis
    elif element == ")":
        while stack[-1] != "(":
            temp = stack.pop()
            output_queu.append(temp)
        # to remove left parenthesis
        stack.pop()

def operator_check(element):
    if element in operator_dict.keys():
        while (len(stack) != 0) and assoc_precedence_check(element) and does_top_of_stack_have_operator():
            temp = stack.pop()
            output_queu.append(temp)
        stack.append(element)

def assoc_precedence_check(element):
    if stack[-1] == "(" or ((operator_assoc[element] == 0) and (operator_dict[element] <= operator_dict[stack[-1]])): return True
    elif stack[-1] == "(" or ((operator_assoc[element]==1) and (operator_dict[element] < operator_dict[stack[-1]])): return True
    else: return False


def does_top_of_stack_have_operator():
    return True if stack[-1] in operator_dict.keys() else False

def empty_stack():
    while len(stack) != 0 :
        temp = stack.pop()
        output_queu.append(temp)

def print_repository():
    print("stack:",stack)
    print("output queu",output_queu)


# main stream
for element in initial_expression:
    # check if it's an operand, if so push it to queu
    operand_check(element)
    # check parenthesis and add push to stack
    parenthesis_check(element)
    # check operator precedence and check left-right assoc. 
    operator_check(element)

    
    # print the results at every 0.25 seconds
    print_repository()
    sleep(0.25)

# after the initial expression is dumped, empty the stack
empty_stack()
# print the final results
print_repository()
# print the postfix expression as text
print("\nPostfix expression ","".join(output_queu))

