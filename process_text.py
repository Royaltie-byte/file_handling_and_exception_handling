with open("first.txt","r") as infile:
    text=infile.read()
    word_count=len(text.split())
    upper_case=text.upper()
with open('output.txt','w') as outfile:
    outfile.write(upper_case)
    outfile.write(f"\nWordcount : {word_count}")
    
    print("Hurray!! the input file has been read successfully and the output file has been written to successfully.")


#Exception handling
test_file=input("Enter the name of a file that you want to read :" )
try:
    with open(test_file,"r") as test:
        data=test.read()
except FileNotFoundError:
    print("The file that you entered does not exist , please check the name of the file again!")
except PermissionError:
    print("Warning!you are not authorized to read this file!")
finally:
    print("Finished trying to read your file.")

