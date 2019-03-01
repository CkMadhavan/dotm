from flask import Flask , render_template,request , redirect , url_for

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
                        if a[0] is not '@':
                            num1 = int(a)
                        if str1[0] is '@' :
                            m = int(addd[a[1 : y.find(',')]])
                        for i in range(0,m) :
                            run (y[y.find(',') + 1 :].strip())
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

@app.route('/help')
def hel():
    return render_template('help.html')

if __name__ == "__main__":
    app.run()
