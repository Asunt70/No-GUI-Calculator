

def calculate():
    history = []
    
    while True:
        question = input("Select: +, -, *, / \nq to exit \nh to show history \nc to clear history \nEnter: ").casefold()
        
        if len(question) == 1:
            if question in ('+', '-', '*', '/'):
                a = float(input("First value: "))
                b = float(input("Second value: "))
                
                if question == '/' and b == 0:
                    print("Error: Cannot divide by zero")
                    continue
                
                if question == '+':
                    result = a + b
                elif question == '-':
                    result = a - b
                elif question == '*':
                    result = a * b
                elif question == '/':
                    result = a / b
                
                if result % 1 == 0:
                    result = int(result)
                
                print("Result:", result)
                
                history.append({'operation': question, 'operand1': a, 'operand2': b, 'result': result})
            
            elif question == 'q':
                break
            
            elif question == 'h':
                print("Calculation History:")
                if history == []:
                    print("No history")
                else:
                    for i, entry in enumerate(history, start=1):
                      print(f"{i}. {entry['operand1']} {entry['operation']} {entry['operand2']} = {entry['result']}")
              
            
            elif question == 'c':
                history.clear()
                print("History cleared!")
        
        else:
            print("Please enter a valid operator")

calculate()