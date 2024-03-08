#Function selects "i" line from selected text file

def DATA(filePath, lineNum):
    with open(filePath, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i == lineNum:
                return line.strip() 
    return "Line number not found in 'data.txt'"

#Function counts the number of lines in the selected text file

def count_lines(filename):
  with open(filename, 'r') as file:
      line_count = 0
      for line in file:
          line_count += 1
      return line_count

#Main function
##d = amount of iterations
##j = name of DataFile

def PassGen(d, j):
  fp1 = j
  fp2 = "passwordFile.txt"

  Ans = input("Has data been collected?[y/n]: ")

  if Ans == "y":
    print("\nExtracting data...\n")
    matrix = list(range(1, count_lines(fp1)+1))

  elif Ans == "n":
    print("\nCollecting data...\n")
    San = input("How many iterations of data do you have?[int]: ")
    with open(j, "w") as file:
      for i in range(int(San)):
         V = input("Data[i]: ")
         file.write(V + "\n")

    matrix = list(range(1, int(San)+1)) 
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
    exit(404)

  with open(fp2, "w") as file:
    for n in range(1, d+1):  
      if n == 1:
        for i in matrix:
          file.write(DATA(fp1, i) + "\n")

      if n == 2:
        for g in matrix:
          for i in matrix:
            file.write(DATA(fp1, g) + DATA(fp1, i) + "\n")

      if n == 3:
        for q in matrix:
          for g in matrix:
            for i in matrix:
              file.write(DATA(fp1, q) + DATA(fp1, g) + DATA(fp1, i) + "\n")

      if n == 4:
        for r in matrix:
          for q in matrix:
            for g in matrix:
              for i in matrix:
                file.write(DATA(fp1, r) + DATA(fp1, q) + DATA(fp1, g) + DATA(fp1, i) + "\n")

#echo -n > passwordFile.txt (to clear 'passwordFile.txt', once done)

if __name__ == "__main__":
  print("Welcome to PassGen!\n")
  print("NUMofExpress?")
  print("ie. = out of 10 ")
  print("*[1] = '~10' possible combinations*")
  print("*[2] = '~110' possible combinations*")
  print("*[3] = '~1110' possible combinations*")
  print("*[4] = '~11110' possible combinations*\n")

  num = int(input("Answer[int]: "))
  PassGen(num, "data.txt")

