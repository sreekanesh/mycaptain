
filename = input("Input the Filename: ")
file_extention = filename.split(".")

#main program
if file_extention[-1]=='py':
    print('your file name is :', filename )
    print('your file extention is : python')

elif file_extention[-1]=='java':
     print('your file name is :', filename )
     print('your file extention is : java')

elif file_extention[-1]=='php':
     print('your file name is :', filename )
     print('your file extention is : php')

else:            
    print('your file name is :', filename )
    print('your file extention is :',file_extention[-1])