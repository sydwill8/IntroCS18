word = input("Word => ")
print(word)
columns = int(input("#columns => "))
print(columns)
rows = int(input("#rows => "))
print(rows)
print("Your word is:", word)
print("\n(a)\n" +  ("*** " * (columns - 1) + "*** \n") * rows)
print("(b)\n" + (("*** " * (columns - 1) + "*** \n") * (rows//2)) +
      (("*** " * (columns // 2)  + "CS1 " + "*** " * (columns // 2) + "\n")) +
      ("*** " * (columns - 1) + "*** \n") * (rows // 2) )

count = 0
while (rows < 6 and count < 1):
    print("(c)\n" + ("*** " * (columns // 2) + " ^ " + " ***" * (columns // 2) + " \n") + 
          ("*** " * ((columns // 2) - 1) + " / "  + " *** " + " \ " + " ***" * ((columns // 2) - 1) + " \n") + 
          ("*** " * ((columns // 2) - 1) + " | " + " CS1 " + " | " + " ***" * ((columns // 2) - 1) + " \n") + 
          ("*** " * ((columns // 2) - 1) + " \ " + " *** " + " / " + " ***" * ((columns // 2) - 1) + " \n") + 
          ("*** " * (columns // 2) + " v " + " ***" * (columns // 2) + " "))
    
    count += 1

while (rows > 6 and rows < 8 and count < 1):
    print("(c)\n" + ("*** " * (columns // 2) + " ^ " + " ***" * (columns // 2) + " \n") +
          (("*** " * ((columns // 2) - 1) + " / "  + " *** " + " \ " + " ***" * ((columns // 2) - 1) + " \n") +
          ("*** " * ((columns // 2) - 1) + " | " + " *** " + " | " + " ***" * ((columns // 2) - 1) + " \n") +
          ("*** " * ((columns // 2) - 1) + " | " + " CS1 " + " | " + " ***" * ((columns // 2) - 1) + " \n") +
          ("*** " * ((columns // 2) - 1) + " | " + " *** " + " | " + " ***" * ((columns // 2) - 1) + " \n") +
          ("*** " * ((columns // 2) - 1) + " \ " + " *** " + " / " + " ***" * ((columns // 2) - 1) + " \n")) + 
          ("*** " * (columns // 2) + " v " + " ***" * (columns // 2) + " "))
    count += 1

while( rows > 8 and count < 1):
    print("(c)\n" + ("*** " * (columns // 2) + " ^ " + " ***" * (columns // 2) + " \n") +
          (("*** " * ((columns // 2) - 1) + " / "  + " *** " + " \ " + " ***" * ((columns // 2) - 1) + " \n") +
          (("*** " * ((columns // 2) - 1) + " | " + " *** " + " | " + " ***" * ((columns // 2) - 1) + " \n") * ((rows - 4) // 2)) +
          ("*** " * ((columns // 2) - 1) + " | " + " CS1 " + " | " + " ***" * ((columns // 2) - 1) + " \n") +
          (("*** " * ((columns // 2) - 1) + " | " + " *** " + " | " + " ***" * ((columns // 2) - 1) + " \n") * ((rows - 4) // 2)) +
          ("*** " * ((columns // 2) - 1) + " \ " + " *** " + " / " + " ***" * ((columns // 2) - 1) + " \n")) + 
          ("*** " * (columns // 2) + " v " + " ***" * (columns // 2) + " "))
    count += 1
    
    

