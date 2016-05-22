from TransformationUtils import *

t = Symbol('t')

def printTableu(tableu):
 print('----------------------')
 for row in tableu:
  print (row)
 print('----------------------')
 return


def pivotOn(z, x_b, tableu, row, col):
 j = 0
 pivot = tableu[row][col - 1]
 x_b[row] = divide_image_values(x_b[row], pivot, 2)
 z_ratio = z[col]
 z[0] -= multiply_image_values(z_ratio, x_b[row], 2)
 for x in tableu[row]:
  tableu[row][j] = divide_image_values(tableu[row][j], pivot, 2)
  j += 1
 for z_j in range(0, len(z) - 1):
  z[z_j + 1] -= multiply_image_values(z_ratio, tableu[row][z_j], 2)

 i = 0
 for xi in tableu:
  if i != row:
   ratio = xi[col - 1]
   j = 0
   x_b[i] -= multiply_image_values(ratio, x_b[row], 2)
   for xij in xi:
    xij -= multiply_image_values(ratio, tableu[row][j], 2)
    tableu[i][j] = xij
    j += 1
  i += 1
 return tableu

# assuming tablue in standard form with basis formed in last m columns
def simplex(z, x_b, tableu, MAX_K):

 THETA_INFINITE = -1
 MAX_ITERATIONS_COUNT = 20
 optimal = False
 unbounded = False
 n = len(z)
 m = len(tableu)
 iteration = 0

 hyper_tableu = [[tableu] * MAX_ITERATIONS_COUNT for x in range(MAX_K + 1)]
 hyper_X = [[x_b] * MAX_ITERATIONS_COUNT for x in range(MAX_K + 1)]
 hyper_Z = [[z] * MAX_ITERATIONS_COUNT for x in range(MAX_K + 1)]

 for j in range(0, MAX_K + 1):
  if j == 0:
   hyper_tableu[iteration][j] = set_matrix_parameter(tableu, 0)
  else:
   hyper_tableu[iteration][j] = differential_transform(tableu, j)
  print(hyper_tableu[iteration][j])

 tableu = hyper_tableu[iteration][0]

 while ((not optimal) and (not unbounded)):
  min = 0.0
  pivotCol = j = 0
  while(j < (n-m)):
   cj = z[j]
     #certain users.
   if (cj < min) and (j > 0):
    min = cj
    pivotCol = j
   j += 1
  if min == 0.0:
   #we cannot profitably bring a column into the basis
   #which means that we've found an optimal solution
   optimal = True
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
    xij = xi[pivotCol - 1]
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
  pivotOn(z, x_b, tableu, pivotRow, pivotCol)

 print ('opt = {}'.format(optimal))
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
x1 = [3.0 * t, 4.0 * t + 2, 8.0 + t,  1.0,  0.0,  0.0]
x2 = [4.0 + t + 2, 5.0 * t, 6.0 * t + 2,   0.0,  1.0,  0.0]
x3 = [7.0 + t, 3.0 * t + 2, 2.0 * t,  0.0,  0.0,  1.0]

tableu = []
tableu.append(x1)
tableu.append(x2)
tableu.append(x3)

MAX_K = 2
tableu = simplex(z, x_b, tableu, MAX_K)

V = 1 / z[0]
print("V = ", V)

length = len(tableu)
strategies = [0 for x in range(length)]
for n in range(1, length):
    strategies[n - 1] = tableu[n][0] * V
print(strategies)
