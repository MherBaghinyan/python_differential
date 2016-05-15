from sympy import *
import numpy as np

t = Symbol('t')

def printTableu(tableu):
 print('----------------------')
 for row in tableu:
  print (row)
 print('----------------------')
 return


def pivotOn(z, x_b, tableu, row, col):
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

def pivotX_b_On(z, x_b, tableu, row, col):
 j = 0
 pivot = tableu[row][col]
 x_b[j] = x_b[0] / pivot
 for x in tableu[row]:
  tableu[row][j] = tableu[row][j] / pivot
  j += 1
 i = 0
 for xi in tableu:
  if i != row:
   ratio = xi[col]
   j = 0
   x_b[i] -= ratio * x_b[i]
   for xij in xi:
    xij -= ratio * tableu[row][j]
    tableu[i][j] = xij
    j += 1
  i += 1
 return x_b

def pivot_z_On(z, tableu, row, col):
 j = 0
 pivot = tableu[row][col]
 for x in tableu[row]:
  tableu[row][j] = tableu[row][j] / pivot
  j += 1
 ratio = z[col]
 j = 0
 for zj in z:
  z[j] -= ratio * tableu[row][j]
  j += 1
 return z


# assuming tablue in standard form with basis formed in last m columns
def simplex(z, x_b, tableu):

 THETA_INFINITE = -1
 opt = False
 unbounded = False
 n = len(z)
 m = len(tableu)
 iteration = 0

 while ((not opt) and (not unbounded)):
  min = 0.0
  pivotCol = j = 0
  while(j < (n-m)):
   cj = z[j]
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
    pivotCol = j - 1
   j += 1
  if min == 0.0:
   #we cannot profitably bring a column into the basis
   #which means that we've found an optimal solution
   opt = True
   continue
  pivotRow = i = 0
  minTheta = THETA_INFINITE
  b_i = 0
  for xi in tableu:
   # Bland's anticycling algorithm  is theoretically a better option than
    #this implementation because it is guaranteed finite while this policy can produce cycling.
    #Kotiath and Steinberg (1978) reported that cylcing does occur in practice
    #contradicting previous reports. For simplicity, I don't use Bland's algorithm here
    #so I just choose smallest xij for pivot row
   if (i > 0):
    xij = xi[pivotCol]
    if xij > 0:
     theta = (x_b[b_i] / xij)
     b_i += 1
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
  newTableu = pivotOn(z, x_b, tableu, pivotRow, pivotCol)
  newX_b = pivotX_b_On(z, x_b, tableu, pivotRow, pivotCol)
  new_z = pivot_z_On(z, tableu, pivotRow, pivotCol)

  tableu = newTableu
  x_b = newX_b
  z = new_z


 print ('opt = {}'.format(opt))
 print ('unbounded = {}'.format(unbounded))
 print ('Final Tableu')
 printTableu(tableu)
 print(x_b)
 print(z)
 iteration += 1
 return tableu

t = Symbol("t")

z = [0.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0]
x_b = [1.0, 1.0, 1.0]
x1 = [3.0 ,  4.0 , 8.0 ,  1.0,  0.0,  0.0]
x2 = [4.0 , 5.0 , 6.0 ,   0.0,  1.0,  0.0]
x3 = [7.0 ,  3.0 , 2.0 ,  0.0,  0.0,  1.0]

tableu = []
tableu.append(x1)
tableu.append(x2)
tableu.append(x3)

tableu = simplex(z, x_b, tableu)

V = 1 / tableu[0][0]
print("V = ", V)

length = len(tableu)
strategies = [0 for x in range(length)]
for n in range(1, length):
    strategies[n - 1] = tableu[n][0] * V
print(strategies)
