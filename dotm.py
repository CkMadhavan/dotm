# This Is The Interactive Shell Of .M Programming Language
# In This You Can Use The display.M() Function To Output The Desired Text on the Screen
# Example : display.M(Hi)
# You Can Use times.M() To Perform A Function n No Of Times
# Example times.M(3,display.M(Hi))
# You Can Use add.M() , sub.M() , mul.M() , over.M() to Add , Subtract , Multiply And Divide Two Numbers Respectively
# Example add.M(3,4) etc.
# You Can Write Multiple Lines Of Code
# Example : display.M(Hi)display.M(Everyone)times.M(2,display.M(Great))mul.M(4,5)display.M(This is .M)
# Write Everything In One Line
# Please Make sure You Do Not Use Unnecessary Space
# Do not Use "" Or ; As You Do In Other Programming Languages
# Please Upvote If You Like (*__*)
from flask import Flask , render_template,request

app = Flask(__name__)

addd = {}

def run(y):
    if y is not "":
        if y[0] is 'd':
            if "display.M(" in y:
                if ")" in y:
                    s = y[y.find('(') + 1:y.find(')')]
                    if s[0] is not '@':
                        text.append (s)
                    else :
                        text.append(addd[s[1:]])
                    lenght = len(s)
                    run(y[y.find(')') + 1:])
                else :
                    text.append("Some Error!")
        
        elif y[0] is 't':        
            if "times.M(" in y:
                if ")" in y:
                    if "," in y:
                        s = y[y.find(')') + 2:].strip()
                        a = y[y.find('(') + 1:y.find(',')].strip()
                        m = int(a)
                        for i in range(0,m) :
                            run (y[y.find(',') + 1 :])
                        run(s)  
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
                    
        elif y[0] is 'a' :
            if "add.M(" in y:
                if ")" in y:
                    if "," in y:
                        str1 = y[y.find('(') + 1 : y.find(',')]
                        str2 = y[y.find(',') + 1 : y.find(')')]
                        if str1[0] is not '@':
                            num1 = int(str1)
                        if str1[0] is '@' :
                            num1 = int(addd[str1[1 : y.find(',')]])
                        if str2[0] is not '@':
                            num2 = int(str2)
                        if str2[0] is '@' :
                            num2 = int(addd[str2[1 : y.find(')')]])
                        add = num1 + num2
                        text.append (add)
                        run(y[y.find(')') + 1 :])
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
                
        elif y[0] is 's' :
            if "sub.M(" in y:
                if ")" in y:
                    if "," in y:
                        str1 = y[y.find('(') + 1 : y.find(',')]
                        str2 = y[y.find(',') + 1 : y.find(')')]
                        if str1[0] is not '@':
                            num1 = int(str1)
                        if str1[0] is '@' :
                            num1 = int(addd[str1[1 : y.find(',')]])
                        if str2[0] is not '@':
                            num2 = int(str2)
                        if str2[0] is '@' :
                            num2 = int(addd[str2[1 : y.find(')')]])
                        dif = num1 - num2
                        text.append (dif)
                        run(y[y.find(')') + 1 :])
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
                        
        elif y[0] is 'm' :
            if "mul.M(" in y:
                if ")" in y:
                    if "," in y:
                        str1 = y[y.find('(') + 1 : y.find(',')]
                        str2 = y[y.find(',') + 1 : y.find(')')]
                        if str1[0] is not '@':
                            num1 = int(str1)
                        if str1[0] is '@' :
                            num1 = int(addd[str1[1 : y.find(',')]])
                        if str2[0] is not '@':
                            num2 = int(str2)
                        if str2[0] is '@' :
                            num2 = int(addd[str2[1 : y.find(')')]])
                        pro = num1 * num2
                        text.append (pro)
                        run(y[y.find(')') + 1 :])
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
                        
        elif y[0] is 'o' :
            if "over.M(" in y:
                if ")" in y:
                    if "," in y:
                        str1 = y[y.find('(') + 1 : y.find(',')]
                        str2 = y[y.find(',') + 1 : y.find(')')]
                        if str1[0] is not '@':
                            num1 = int(str1)
                        if str1[0] is '@' :
                            num1 = int(addd[str1[1 : y.find(',')]])
                        if str2[0] is not '@':
                            num2 = int(str2)
                        if str2[0] is '@' :
                            num2 = int(addd[str2[1 : y.find(')')]])
                        divi = num1 / num2
                        text.append (divi)
                        run(y[y.find(')') + 1 :])       
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
        
        elif y[0] is 'v' :
            if "var.M(" in y:
                if ")" in y:
                    if "@" in y:
                        varname = y[y.find('@') + 1 : y.find(')')]
                        addd.update({varname : 0})
                        run(y[y.find(')') + 1 :])       
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
                    
        elif y[0] is 'e' :
            if "equals.M(" in y:
                if ")" in y:
                    if "," in y:
                        if "@" in y:
                            varname = y[y.find('@') + 1 : y.find(',')]
                            num = y[y.find(',') + 1 : y.find(')')].strip()
                            addd.update({varname : num})
                            run(y[y.find(')') + 1 :]) 
                        else :
                            text.append("Some Error!")
                    else :
                        text.append("Some Error!")
                else :
                    text.append("Some Error!")
                

text = []

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/output' , methods = ["POST"])
def out():
    
    text.clear()
    process_text = request.form['program']
    process_text = "".join( process_text.splitlines())
    run(process_text)
    print(process_text)
    return render_template('temp.html' , v=text)

if __name__ == "__main__":
    app.run()
