from TransformationUtils import *

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
  tableu[row][j] = divide_image_values(tableu[row][j], pivot, 2)
  j += 1
 i = 0
 for xi in tableu:
  if i != row:
   ratio = xi[col]
   j = 0
   for xij in xi:
    xij -= multiply_image_values(ratio, tableu[row][j], 2)
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
   cj = item_transform(tableu[0][j], 2)
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
    if item_transform(xij, 2) > 0:
     theta = divide_image_values(xi[0], xij, 2)
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

t = Symbol("t")

z  = [ 0.0 , -1.0 *t , -1.0 ,-1.0 * t**2, 0.0,  0.0,  0.0]
x1 = [1.0 ,  3.0*t**2 ,  4.0*t , 8.0*t**2 ,  1.0,  0.0,  0.0]
x2 = [1.0 , 4.0 , 5.0 , 6.0*t**2 ,   0.0,  1.0,  0.0]
x3 = [1.0 ,  7.0*t ,  3.0 , 2.0*sin(t) ,  0.0,  0.0,  1.0]

tableau = []
tableau.append(z)
tableau.append(x1)
tableau.append(x2)
tableau.append(x3)

tableau = simplex(tableau)

V = 1 / item_transform(tableau[0][0], 2)
print("V = ", V)

length = len(tableau)
strategies = [0 for x in range(length)]
for n in range(1, length):
    strategies[n - 1] = tableau[n][0] * V
print(strategies)
