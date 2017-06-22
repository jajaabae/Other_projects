#-*-coding:utf8;-*-

# makes generic function from name "n"
def makeFun(funName):
    strFun = """global fun_%s
def fun_%s(inn):
        print "function name: %s "
        print "function name's length:", len('%s')
        print 'input value was: ', inn
        print
    """
    param = funName , funName , funName , funName
    exec(strFun % param)
    
    
# runs generic function with name "n" and input "x"
def execFun(funName, inn):
    execStr = """fun_%s(inn)
    """
    string = execStr % funName
    exec(string)

print
print 'Manual definition and call of solution function:'
makeFun('solution')
fun_solution(42)


print
# functiones to be made and run
print 'Generating and running functions from list:'
funNames = [
    'aaaaaaa',
    'bb',
    'cccc',
    'd',
    'eeeeeeeeeeee',
    ]
    
    
for n in funNames:
    makeFun(n)
    
baseVal=1
for n in funNames:
    innVal = baseVal
    baseVal+=1
    execFun(n, innVal)


