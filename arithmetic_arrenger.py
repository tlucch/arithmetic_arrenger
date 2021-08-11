def arithmetic_arranger(problems, solve = False):

  import re
  top = ''
  mid = ''
  lines = ''
  bottom = ''

  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for problemas in problems:
      [num1, oper, num2] = problemas.split()

      if oper != "+" and oper != "-":
        return "Error: Operator must be '+' or '-'."
      elif not (re.search('^\d+$', num1, 0) and re.search('^\d+$', num2, 0)):
        return 'Error: Numbers must only contain digits.'
      elif len(num1) > 4 or len(num2) > 4:
        return "Error: Numbers cannot be more than four digits."

      else:
        if oper == "+":
          result = int(num1) + int(num2)
        elif oper == "-":
          result = int(num1) - int(num2)

        maxlength = max(len(num1), len(num2))
        top = top + "  " + num1.rjust(maxlength) + "    "
        mid = mid + oper + " " + num2.rjust(maxlength) + "    "
        lines = lines + "-"*(maxlength + 2) + "    "
        bottom = bottom + str(result).rjust(maxlength + 2) + "    "
      
  if solve == False:
    arranged_problems = top.rstrip() + "\n" + mid.rstrip() + "\n" + lines.rstrip()
  if solve == True:
    arranged_problems = top.rstrip() + "\n" + mid.rstrip() + "\n" + lines.rstrip() + "\n" + bottom.rstrip()

  return arranged_problems
  
  

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
