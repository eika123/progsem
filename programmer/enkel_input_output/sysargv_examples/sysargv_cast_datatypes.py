import sys

 
# Remember: the data type of elements in sys.argv are always strings!
# sometimes one must change the datatype, for example to float
# in order to do calculations


number1 = float(sys.argv[1])
number2 = float(sys.argv[2])

result = number1*number2

print(result)
