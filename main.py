numbers = []
for i in range(1, 129):
  numbers.append(i)

print("Think of a number between 1 and 128.")
print("")
print("I will try to guess the number you are thinking about and you just need to tell me if my guess was too high or too low. And if the number is correct, just write: correct.")
print("")

user_ok = input("Ok? (write ok to begin)?\n").lower()

if user_ok == "ok":
  print("64?")
  user_answer = input("too high / too low\n").lower()
  if user_answer == "too high":
    del numbers[63:128]
    
    print("32?")
    user_answer = input("too high / too low\n").lower()
    if user_answer == "too high":
      del numbers[31:64]
  
      print("16?")
      user_answer = input("too high / too low\n").lower()
      if user_answer == "too high":
        del numbers[15:32]
  
        print("8?")
        user_answer = input("too high / too low\n").lower()
        if user_answer == "too high":
          del numbers[7:16]
  
          print("4?")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[3:8]
            
            print("2?")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 1")
            elif user_answer == "too low":
              print("Your number is: 3")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[0:4]
          
            print("6?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 5")
            elif user_answer == "too low":
              print("Your number is: 7")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[0:8]
  
          print("12?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[13:16]
  
            print("10?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 9")
            elif user_answer == "too low":
              print("Your number is: 11")
            else:
              print("Thank you for playing.")

          elif user_answer == "too low":
            del numbers[0:12]

            print("14?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 13")
            elif user_answer == "too low":
              print("Your number is: 15")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")

        else:
          print("Thank you for playing.")
      
      elif user_answer == "too low":
        del numbers[0:16]
  
        print("24?")
        user_answer = input("too high / too low\n")
        if user_answer == "too high":
          del numbers[25:32]
        
          print("20?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[21:24]
  
            print("18?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 17")
            elif user_answer == "too low":
              print("Your number is: 19")
            else:
              print("Thank you for playing.")
              
          elif user_answer == "too low":
            del numbers[15:20]
  
            print("22?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 21")
            elif user_answer == "low":
              print("your number is: 23")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[2:24]
  
          print("28?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[29:32]

            print("26?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 25")
            elif user_answer == "too low":
              print("your number is: 27")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[25:28]

            print("30?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 29")
            elif user_answer == "low":
              print("your number is: 31")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")

        else:
          print("Thank you for playing.")

      else:
        print("Thank you for playing.")
    
    elif user_answer == "too low":
      del numbers[0:32]
  
      print("48?")
      user_answer = input("too high / too low\n")
      if user_answer == "too high":
        del numbers[49:64]
  
        print("40?")
        user_answer = input("too high / too low\n")
        if user_answer == "too high":
          del numbers[41:48]
  
          print("36?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[35:40]
  
            print("34?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 33")
            elif user_answer == "too low":
              print("Your number is: 35")
            else:
              print("Thank you for playing.")
            
          elif user_answer == "too low":
            del numbers[33:36]
  
            print("38?")
            user_answer = input("too high / too low\n")
            if user_answer == "yes":
              print("Your number is: 37")
            elif user_answer == "too low":
              print("Your number is: 39")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[31:40]
  
          print("44?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[45:48]
  
            print("42?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 41")
            elif user_answer == "too low":
              print("Your number is: 43")
            else:
              print("Thank you for playing.")
                
          elif user_answer == "too low":
            del numbers[41:44]
  
            print("46?")
            user_answer  = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 45")
            elif user_answer == "too low":
              print("Your number is: 47")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")

        else:
          print("Thank you for playing.")
      
      elif user_answer == "too low":
        del numbers[31:48]  
        
        print("56?")
        user_answer = input("too high / too low\n")
        if user_answer == "too high":
          del numbers[57:64]
          
          print("52?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[53:56]
  
            print("50?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 49")
            elif user_answer == "too low":
              print("Your number is: 51")
            else:
              print("Thank you for playing.")
  
          elif user_answer == "too low":
            del numbers[49:52]  
          
            print("54?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 53")
            elif user_answer == "too low":
              print("Your number is: 55")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[49:56]
          
          print("60?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[61:64]
  
            print("58")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 57")
            elif user_answer == "too low":
              print("Your number is: 59")
            else:
              print("Thank you for playing.")
  
          elif user_answer == "too low":
            del numbers[57:60]
            
            print("62")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 61")
            elif user_answer == "too low":
              print("Your number is: 63")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")

        else:
          print("Thank you for playing.")

      else:
        print("Thank you for playing.")

    else:
      print("Thank you for playing.")  
  elif user_answer == "too low":
    del numbers[0:64]
   
    print("96?")
    user_answer = input("too high / too low\n").lower()
    if user_answer == "too high":
      del numbers[97:128]
  
      print("80?")
      user_answer = input("too high / too low\n").lower()
      if user_answer == "too high":
        del numbers[81:96]
  
        print("72?")
        user_answer = input("too high / too low\n").lower()
        if user_answer == "too high":
          del numbers[73:80]
  
          print("68?")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[69:72]
  
            print("66?")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 65")
            elif user_answer == "too low":
              print("Your number is: 67")
            else:
              print("Thank you for playing!")
          
          elif user_answer == "too low":
            del numbers[65:68]             
            
            print("70")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 69")
            elif user_answer == "too low":
              print("Your number is: 71")
            else:
              print("Thank you for playing.")
          
          else:
            print("Thank you for playing!")
        
        elif user_answer == "too low":
          del numbers[65:72]
  
          print("76?")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[77:80]
  
            print("74?")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 73")
            elif user_answer == "too low":
              print("Your number is: 75")
            else:
              print("Thank you for playing!")
          
          elif user_answer == "too low":
            del numbers[73:76]
  
            print("78?")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 77")
            elif user_answer == "too low":
              print("Your number is: 79")
            else:
              print("Thank you for playing!")
      
          else:
            print("Thank you for playing!")

        else:
          print("Thank you for playing!")
      
      elif user_answer == "too low":
        del numbers[65:80]
        
        print("88?")
        user_answer = input("too high / too low\n").lower()
        if user_answer == "too high":
          del numbers[89:96]
  
          print("84?")
          user_answer = input("too high / too low\n")
          if user_answer == "too high":
            del numbers[85:88]
  
            print("82?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("You number is: 81")
            elif user_answer == "too low":
              print("Your number is: 83")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[81:84]
  
            print("86?")
            user_answer = input("too high / too low\n")
            if user_answer == "too high":
              print("Your number is: 85")
            elif user_answer == "too low":
              print("Your number is: 87")
            else:
              print("Thank you for playing!")

          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[81:88]
  
          print("92?")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[93:96]
  
            print("90?")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 89")
            elif user_answer == "too low":
              print("your number is: 91")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[89:92]
  
            print("94?")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 93")
            elif user_answer == "too low":
              print("your number is: 95")
            else:
              print("Thank you for playing!")
              
          else:
            print("Thank you for playing!")

        else:
          print("Thank you for playing!")

      else:
        print("Thank you for playing.")
    
    elif user_answer == "too low":
      del numbers[65:96]
    
      print("112?")
      user_answer = input("too high / too low\n").lower()
      if user_answer == "too high":
        del numbers[113:128]
    
        print("104")
        user_answer = input("too high / too low\n").lower()
        if user_answer == "too high":
          del numbers[105:112]    
    
          print("100")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[101:104]
    
            print("98")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 97")
            elif uder_answer == "too low":
              print("Your number is: 99")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[97:100]
    
            print("102")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 101")
            elif uder_answer == "too low":
              print("Your number is: 103")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[97:104]
    
          print("108")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[109:112]
    
            print("106")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 105")
            elif user_answer == "too low":
              print("Your number is: 107")
            else:
              print("Thank you for playing!")
          
          elif user_answer == "too low":
            del numbers[105:108]
    
            print("110")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 109")
            elif uder_answer == "too low":
              print("Your number is: 111")
            else:
              print("Thank you for playing.")

          else:
            print("Thank you for playing.")
      
        else:
          print("Thank you for playing.")
      
      elif user_answer == "too low":
        del numbers[97:112]
    
        print("120")
        user_answer = input("too high / too low\n").lower()
        if user_answer == "too high":
          del numbers[121:128]
    
          print("116")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[117:120]
    
            print("114")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 113")
            elif uder_answer == "too low":
              print("Your number is: 115")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[113:116]
    
            print("118")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 116")
            elif user_answer == "too low":
              print("Your number is: 119")
            else:
              print("Thank you for playing.")
          else:
            print("Thank you for playing.")
        
        elif user_answer == "too low":
          del numbers[113:120]
    
          print("124")
          user_answer = input("too high / too low\n").lower()
          if user_answer == "too high":
            del numbers[125:128]
    
            print("122")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 121")
            elif user_answer == "too low":
              print("Your number is: 123")
            else:
              print("Thank you for playing.")
          
          elif user_answer == "too low":
            del numbers[121:124]
    
            print("126")
            user_answer = input("too high / too low\n").lower()
            if user_answer == "too high":
              print("Your number is: 125")
            elif user_answer == "too low":
              print("Your number is: 127")
            else:
              print("Thank you for playing.")
          else:
            print("Thank you for playing.")
        else:
          print("Thank you for playing.")
      else:
        print("Thank you for playing.")
  
    else:
      print("Thank you for playing!")
  else:
    print("Thank you for playing!")