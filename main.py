import random

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        time_now = time.time()
        res = func(*args,**kwargs)
        print(round(time.time()-time_now,2),'seconds')
        return res
    return wrapper


def gen_rand_matrix(n=50, m=50, min_limit=-250, max_limit=1001):
    a = []
    for i in range(n):
        t = []
        for j in range(m):
            t.append(random.randint(min_limit, max_limit))
        a.append(t)
    return (a)



a = gen_rand_matrix(5, 5, -10, 10)



@time_it
def selection_sort(result):
    res = []
    #print (result)
    for k in result:

        arr = k
        for i in range (len(k)-1):
            min_value = arr[i]
            p=i
            for j in range (i+1, len(k)):
                if arr[j] < min_value:
                    min_value = arr[j]
                    p=j
            arr[p], arr[i] = arr[i], arr[p]
        res.append(arr)
    return res
        # print (arr)

#selection_sort(a)

@time_it
def insert_sort(result):
    # print (result)
    res = []
    for k in result:
        arr = k
        for i in range (1, len(k)):
            current_value = arr[i]
            current_position = i
            while (current_position>0) and (current_value < arr[current_position-1]):
                arr[current_position] = arr[current_position-1]
                current_position -= 1
            arr[current_position] = current_value
        res.append(arr)
    return res
        # print (arr)

#insert_sort(a)

@time_it
def buble_sort(result):
    # print (result)
    res=[]
    for k in result:
        arr = k
        buble = len(k)
        while buble > 1:
            for i in range(buble-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1],arr[i]
            buble -= 1
        res.append(arr)
    return res
        # print (arr)
#buble_sort(a)

@time_it
def shell_sort(result):
    res=[]
    # print (result)
    for k in result:
        arr = k

        diapason = len(k)//2
        while diapason > 0:
            for i in range(diapason, len(k)):
                current_value = arr[i]
                position = i
                while position >= diapason and arr[position-diapason] > current_value:
                    arr[position] = arr[position-diapason]
                    position -= diapason
                    arr[position] = current_value


            diapason //= 2
        res.append(arr)
    return res
#shell_sort(a)


import heapq
from queue import Queue

def turnir_sort(arr):

    queue_ = Queue()
    for element in arr:
        queue_.put(element)
    winners = []
    losers = []
    mini_heap = []
    for i in range(min(7, len(arr))):
        mini_heap.append(queue_.get())
    heapq.heapify(mini_heap)
    while mini_heap:
        heap_min = heapq.heappop(mini_heap)
        if not winners or heap_min >= winners[-1]:
            winners.append(heap_min)
        else:
            losers.append(heap_min)
        if not queue_.empty():
            heapq.heappush(mini_heap, queue_.get())
    if losers:
        return turnir_sort(losers + winners)
    return losers + winners

@time_it
def sort_tournament(result):
    #print (resultФ
    arr = []
    for k in result:
        # print(type(k))
        arr.append(turnir_sort(k.copy()))
        #print(turnir_sort(arr))
    return arr

#sort_tournament(a)



def quick1_sort (arr):
    if len(arr) <= 1:
        return arr

    elem = arr[0]
    left = list(filter(lambda x: x < elem, arr))
    center = [i for i in arr if i == elem]
    right = list(filter(lambda x: x > elem, arr))

    return quick1_sort(left) + center + quick1_sort(right)

@time_it
def quick_sort(result):
    #print (result)
    arr=[]
    for k in result:
        arr.append(quick1_sort(k))
        #print(quick1_sort(arr))
    return arr
#quick_sort(a)


@time_it
def heap_sort(result):
    #print (result)
    res=[]
    for k in result:
        arr = k
        length = len(arr)

        def swap_items(index1, index2): # меняем местами два элемента
            if arr[index1] < arr[index2]:
                arr[index1], arr[index2] = arr[index2], arr[index1]

        def max_find (parent, limit): #ищем максимальный среди родителей и потомков

            while True:
                child = parent * 2 + 2
                if child < limit:
                    if arr[child] < arr[child - 1]:
                        child -= 1
                    swap_items(parent, child)
                    parent = child
                else:
                    break

        for index in range(int(length // 2) - 1, -1, -1): # формируем первое дерево
            max_find(index, length)

        for index in range(length - 1, 0, -1): #выносим максимальный назад и ставим минимум на свое место
            swap_items(index, 0)
            max_find(0, index)
        res.append(arr)
    return res
        #print(arr)

#heap_sort(a)


@time_it
def default_sort(result):
    #print (result)
    res = []
    for k in result:
        arr = k
        mass = sorted(arr)
        res.append(mass)
        #print(res)
    return res







import copy

result1 = gen_rand_matrix(100,100)
print ('Сортировка Шелла:', end=' ')
a=shell_sort(copy.deepcopy(result1))
print ('Сортировка обменом:', end=' ')
b=buble_sort(copy.deepcopy(result1))
print ('Сортировка вставками:', end=' ')
c=insert_sort(copy.deepcopy(result1))
print ('Сортировка выбором:', end=' ')
d=selection_sort(copy.deepcopy(result1))
print ('Турнирная сортировка:', end=' ')
e=sort_tournament(copy.deepcopy(result1))
print ('Быстрая сортировка:', end=' ')
f=quick_sort(copy.deepcopy(result1))
print ('Сортировка кучей:', end=' ')
g=heap_sort(copy.deepcopy(result1))
print ('Встроенная сортировка:', end=' ')
h=default_sort(copy.deepcopy(result1))
for i in range(100):
    for j in range(100):
        if a[i][j] == b[i][j] and a[i][j] == c[i][j] and a[i][j] == d[i][j] and a[i][j] == e[i][j] and a[i][j] == f[i][j] and a[i][j] == g[i][j]:
            pass
        else:
            print('ploho') # no vse horosho :)