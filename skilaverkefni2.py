# 1
'''
O(n)
'''
# 2
bubbleSort(arr[], n)
{
    for (i = 0; i < n-1; i++)
        Last i elements are already in place
        for (j = 0; j  arr[j+1])
            swap(arr[j], arr[j+1]);
}

# 3
def recursive_print(curser):
  alphabet = 'abcdef'
  index = len(alphabet) - curser
  if index > 0:
    recursive_print(index - 1)

  letter = alphabet[index]
  print(letter)

print(recursive_print(0))



# 4
'''
def fall(L):
    hæsta = max(L)
    countL = [0]*(hæsta+1)
    resultL = [0]*len(L)

    for i in L:
        countL[i] += 1

        summa = 0
        for i in range(len(countL)):
            summa+= countL[i]
            countL[i] = summa

        for i in range(len(L)):
            resultL[countL[L[i]]-1] = L[i]
            countL[L[i]] -= 1
        return resultL

L = [7,1,8,2,5,10,8,9,3,6,1]
print(fall(L))
'''

# 5

'''
number = [1,2,3,4,5,6,]

def radalista(number):
    if number > 1:
        return [number] + radalista(number-1)
    else:
        return [number]

numer = int(input("Sláðu inn tölu: "))
radalista(numer)
print(number)
'''


