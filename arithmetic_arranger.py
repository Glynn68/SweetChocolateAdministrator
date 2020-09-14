def arithmetic_arranger(problems, ans = False):
  print (problems)
  #
  #Test for too many problems
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
  #
  #Test for each operator either + or -
  for a in problems:
    sum = a.split()
    if sum[1] != "+" and sum[1] != "-":
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
  #
  # Test that operands are all digits
  for a in problems:
    sum = a.split()
    for b in range (0, 3, 2):
      if sum[b].isdigit() == False:
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems
  #
  # Test if any operands have more than 4 digits
  for a in problems:
    sum = a.split()
    for b in range (0, 3, 2):
      if len(sum[b]) > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems  
  #
  # Make lists of upper & lower operands, operators, dashes and answers
  upper_opp = []
  lower_opp = []
  operator = []
  dashes = []
  answers = []
  for a in problems:
    sum = a.split()
    upper_opp.append(int(sum[0]))
    operator.append(sum[1])
    lower_opp.append(int(sum[2]))
  #
  # Make list of answers
  for a in range (len(problems)):
    if operator[a] == "-":
      x = upper_opp[a] - lower_opp[a]
    else:
      x = upper_opp[a] + lower_opp[a]
    answers.append(x)
  # 
  # Add correct number of spaces before upper & lower operands
  for a in range (len(problems)):
    upper_opp[a] = str(upper_opp[a])
    lower_opp[a] = str(lower_opp[a])
    max_char = max(len(upper_opp[a]), len(lower_opp[a]))
    d = max_char - len(upper_opp[a]) + 2
    for c in range (d):
      upper_opp[a] = ' ' + upper_opp[a]
    e = max_char - len(lower_opp[a])
    for c in range (e):
      lower_opp[a] = ' ' + lower_opp[a]
    lower_opp[a] = operator[a] + ' ' + lower_opp[a]
    #Make list of dashes
    g = '-'
    for f in range(max_char +1):
      g = g + '-'
    dashes.append(g)
    #Add correct num of spaces to answers
    answers[a] = str(answers[a])
    max_char_2 = max(max_char, len(answers[a]))
    h = max_char_2 -len(answers[a])
    if int(answers[a]) > -1:
      for c in range(h+2):
        answers[a] = ' ' + answers[a]
    else:
      for c in range(h+1):
        answers[a] = ' ' + answers[a]
  #
  #concatenate lists
  upper = '    '.join(upper_opp)
  lower = '    '.join(lower_opp)
  dashes_fin = '    '.join(dashes)
  ans_fin = '    '.join(answers)
  arranged_problems = upper + '\n' + lower + '\n' + dashes_fin
  if ans:
    arranged_problems = arranged_problems + '\n' + ans_fin
  print(arranged_problems)
  return arranged_problems