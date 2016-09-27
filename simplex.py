def printTableu(tableu):
 print('----------------------')
 for row in tableu:
  print (row)
 print('----------------------')
 return


def pivotOn(tableu, row, col):
 j = 0
 pivot = tableu[row][col]
 for x in tableu[row]:
  tableu[row][j] = tableu[row][j] / pivot
  j += 1
 i = 0
 for xi in tableu:
  if i != row:
   ratio = xi[col]
   j = 0
   for xij in xi:
    xij -= ratio * tableu[row][j]
    tableu[i][j] = xij
    j += 1
  i += 1
 return tableu


# assuming tablue in standard form with basis formed in last m columns
def simplex(tableu):

 THETA_INFINITE = -1
 opt   = False
 unbounded  = False
 n = len(tableu[0])
 m = len(tableu) - 1

 while ((not opt) and (not unbounded)):
  min = 0.0
  pivotCol = j = 0
  while(j < (n-m)):
   cj = tableu[0][j]
   # we will simply choose the most negative column
    #which is called: "the nonbasic gradient method"
    #other methods as "all-variable method" could be used
    #but the nonbacis gradient method is simpler
    #and all-variable method has only been shown to be superior for some
     #extensive experiments by Kuhn and Quandt, the random tests used
     #by Kuhn and Quandt might not really represent "typical" LP's for
     #certain users.
   if (cj < min) and (j > 0):
    min = cj
    pivotCol = j
   j += 1
  if min == 0.0:
   #we cannot profitably bring a column into the basis
   #which means that we've found an optimal solution
   opt = True
   continue
  pivotRow = i = 0
  minTheta = THETA_INFINITE
  for xi in tableu:
   # Bland's anticycling algorithm  is theoretically a better option than
    #this implementation because it is guaranteed finite while this policy can produce cycling.
    #Kotiath and Steinberg (1978) reported that cylcing does occur in practice
    #contradicting previous reports. For simplicity, I don't use Bland's algorithm here
    #so I just choose smallest xij for pivot row
   if (i > 0):
    xij = xi[pivotCol]
    if xij > 0:
     theta = (xi[0] / xij)
     if (theta < minTheta) or (minTheta == THETA_INFINITE):
      minTheta = theta
      pivotRow = i
   i += 1
  if minTheta == THETA_INFINITE:
   #bringing pivotCol into the basis
   #we can move through that vector indefinetly without
   #becoming unfesible so the polytope is not bounded in all directions
   unbounded = True
   continue

  #now we pivot on pivotRow and pivotCol
  tableu = pivotOn(tableu, pivotRow, pivotCol)
 print ('opt = {}'.format(opt))
 print ('unbounded = {}'.format(unbounded))
 print ('Final Tableu')
 printTableu(tableu)
 return tableu


z  = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  0.0,  0.0,  0.0,  0.0]
x1 = [1.0,  7.97866636527875e-5, 0.000137193917321702, 9.14627721639419e-5, 5.09044466794337e-5, 0.000108172178261904, 4.03224557756208e-5, 6.39201407556726e-5, 0.000109222384775335, 4.82830827614442e-5, 8.45859166749473e-5,  1.0,  0.0,  0.0,  0.0,  0.0, 0.0,  0.0,  0.0,  0.0, 0.0]
x2 = [1.0,  6.98753389171327e-5, 5.56928707976882e-5, 9.14627721639419e-5, 0.000138884938383975, 0.000108172178261904, 4.91264522041279e-5, 6.39201407556726e-5, 4.44662513089283e-5, 6.90180390700260e-5, 9.14627721639419e-5,   0.0,  1.0,  0.0,  0.0,  0.0, 0.0,  0.0,  0.0,  0.0, 0.0]
x3 = [1.0,  0.000138887160515336, 5.56928707976882e-5, 9.14627721639419e-5, 4.00352589279837e-5, 0.000108172178261904, 4.91264522041279e-5, 6.39201407556726e-5, 9.14627721639419e-5, 4.82830827614442e-5, 6.14751195928780e-5,  0.0,  0.0,  1.0,  0.0,  0.0, 0.0,  0.0,  0.0,  0.0, 0.0]
x4 = [1.0,  9.29744320807641e-5, 5.85935302742615e-5, 3.71286069996157e-5, 5.09044466794337e-5, 5.51468252605048e-5, 6.65677070147996e-5, 7.21149852093127e-5, 0.000109222384775335, 4.82830827614442e-5, 8.45859166749473e-5,  0.0,  0.0,  0.0,  1.0,  0.0, 0.0,  0.0,  0.0,  0.0, 0.0]
x5 = [1.0,  6.21543499912442e-5, 6.18129422784701e-5, 9.14627721639419e-5, 5.09044466794337e-5, 0.000108172178261904, 3.64076651902177e-5, 6.39201407556726e-5, 8.45859166749473e-5, 4.82830827614442e-5, 3.71286069996157e-5,  0.0,  0.0,  0.0,  0.0,  1.0, 0.0,  0.0,  0.0,  0.0, 0.0]
x6 = [1.0,  0.000123625004241711, 7.92249504087021e-5, 9.14627721639419e-5, 5.09044466794337e-5, 0.000119679751028671, 4.03224557756208e-5, 4.76693170072462e-5, 0.000109222384775335, 4.82830827614442e-5, 8.45859166749473e-5,  0.0,  0.0,  0.0,  0.0,  0.0, 1.0,  0.0,  0.0,  0.0, 0.0]
x7 = [1.0,  4.66803026815556e-5, 7.92249504087021e-5, 3.97525288120675e-5, 5.09044466794337e-5, 6.11410172508755e-5, 0.000103210191067843, 6.39201407556726e-5, 0.000109222384775335, 4.82830827614442e-5, 3.97525288120675e-5,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  1.0,  0.0,  0.0, 0.0]
x8 = [1.0,  3.73752901186298e-5, 5.30658575121820e-5, 6.90180390700260e-5, 4.00352589279837e-5, 7.81245312528125e-5, 4.03224557756208e-5, 6.39201407556726e-5, 3.09916617719125e-5, 4.82830827614442e-5, 7.86708533453336e-5,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  0.0,  1.0,  0.0, 0.0]
x9 = [1.0,  6.21543499912442e-5, 3.60576090978252e-5, 9.14627721639419e-5, 5.09044466794337e-5, 3.82651936696349e-5, 3.22348772179544e-5, 6.39201407556726e-5, 4.27755248743213e-5, 4.82830827614442e-5, 6.90180390700260e-5,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  0.0,  0.0,  1.0, 0.0]
x10 = [1.0, 7.97866636527875e-5, 0.000216343158325500, 9.14627721639419e-5, 5.09044466794337e-5, 6.11410172508755e-5, 4.03224557756208e-5, 6.39201407556726e-5, 6.90180390700260e-5, 0.000109222384775335, 8.45859166749473e-5,  0.0,  0.0,  0.0,  0.0,  0.0, 0.0,  0.0,  0.0,  0.0, 1.0]


tableu = []
tableu.append(z)
tableu.append(x1)
tableu.append(x2)
tableu.append(x3)
tableu.append(x4)
tableu.append(x5)
tableu.append(x6)
tableu.append(x7)
tableu.append(x8)
tableu.append(x9)
tableu.append(x10)

tableu = simplex(tableu)

print('----------------------------------------------')
#print((0.4 * (9.2 ** 2) + 0.4 *(9.1 ** 2) + 0.4 *(28 ** 2)) ** -1/2)
#print((0.4 * (1.2 ** 2) + 0.4 *(0.7 ** 2) + 0.4 *(1.1 ** 2)) ** -1/2)

V = 1 / tableu[0][0]
print("V = ", V)

length = len(tableu)
strategies = [0 for x in range(length)]
for n in range(1, length):
    strategies[n - 1] = tableu[n][0] * V
    print(tableu[n][0])
print(strategies)
