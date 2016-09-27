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
 x_b[row] = x_b[row] / pivot
 z_ratio = z[col]
 z[0] -= z_ratio * x_b[row]
 for x in tableu[row]:
  tableu[row][j] = tableu[row][j] / pivot
  j += 1
 for z_j in range(0, len(z) - 1):
  z[z_j + 1] -= z_ratio * tableu[row][z_j]

 i = 0
 for xi in tableu:
  if i != row:
   ratio = xi[col - 1]
   j = 0
   x_b[i] -= ratio * x_b[row]
   for xij in xi:
    xij -= ratio * tableu[row][j]
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

 hyper_X = [[x_b] * MAX_ITERATIONS_COUNT for x in range(MAX_K + 1)]
 hyper_Z = [[z] * MAX_ITERATIONS_COUNT for x in range(MAX_K + 1)]

 for j in range(0, MAX_K + 1):
  hyper_X[iteration][j] = differential_vector(x_b, j)
  print(hyper_X[iteration][j])

 x_b = hyper_X[iteration][0]

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
  if iteration == 0:
   pivotOn(z, x_b, tableu, pivotRow, pivotCol)
  else:
   for k in range(1, MAX_K + 1):
    pivotOn(hyper_Z[iteration][k-1], hyper_X[iteration][k-1], tableu, pivotRow, pivotCol)

 print ('opt = {}'.format(optimal))
 print ('unbounded = {}'.format(unbounded))
 print ('Final Tableu')
 printTableu(tableu)
 print(x_b)
 print(z)
 iteration += 1
 return tableu

t = Symbol("t")

#  max r1 + r2 + r3

#  179.95r1 + 156.12r2 + 90r3 ≤ 1 + 0.1504(1 − α)

#  89.95r1 + 179.87r2 + 155r3 ≤ 1 + 0.1504(1 − α)

#  180r1 + 156r2 + 177r3 ≤ 1 + 0.1504(1 − α)

#  r1, r2, r3 ≥ 0, α ∈]0, 1].


z = [0.0, -1.0, -1.0, -1.0, 0.0,  0.0,  0.0]
x_b = [1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t), 1 + 0.1504*(1 - t)]
x1 = [179.95, 156.12, 90,  1.0,  0.0,  0.0]
x2 = [89.95, 179.87, 155,   0.0,  1.0,  0.0]
x3 = [180, 156, 177,  0.0,  0.0,  1.0]

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