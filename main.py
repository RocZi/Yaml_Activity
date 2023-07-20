import calculator

selection = int( input("\nSelect your calculator operation:    \nl. Addition     \n2. Subtraction     \n3. Multiplication     \n4. Division\n"))

numl, num2 = int( input( "\nProvide your 2 values:")) 

if selection== 1: 
    calculator.add()

if selection== 2: 
    calculator.subtract()

if selection== 3: 
    calculator.multiply()

if selection== 4: 
    calculator.divide()