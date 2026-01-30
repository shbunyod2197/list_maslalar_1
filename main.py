# 1
number = [10, 20, 30, 40, 50]

print(len(number))
print([3])
print(number.count(30))
new_roy = number[-2: ]
print(new_roy)
sum = sum(number)
print(sum)
# 2
fruits = ['apple', 'banana', 'cherry']

fruits.append('kiwi')
print(fruits)
fruits.pop(1)
print(fruits)
fruits.insert(2,"peach")
print(fruits)
fruits.sort()
print(fruits)
# 3
scores = [85, 90, 78, 92, 88]
sum = sum(scores)
print(scores)
orta_summ = sum / 2
print(orta_summ)
print(max(scores))
scores.sort(reverse=True)
print(scores)
# 4
items = [1, 2, 2, 3, 3, 4, 1]
a = set(items)
print(set(a))

n_items = items
print(n_items)

items.sort()
print(items[1::-1])

print(len(items))

print(items)
# 5
list1 = [1, 3, 5]
list2 = [2, 4, 6]

list1.extend(list2)
print(list1)

list1.sort()
print(list1)

new_list = list2
print(new_list)

summ = sum(new_list)
print(summ)

print(new_list)
# 6
values = [12, 5, 8, 19, 3, 15]

print(max(values))
print(min(values))

m = values.index(max(values))
print(m)

m = values.index(min(values))
print(m)

print(values)
# 7
words = ['apple', 'cherry', 'banana', 'date']
print(words)
nw_r = words

nw_r.reverse()
print(nw_r)

nw_r.sort()
print(nw_r)

print(len(nw_r))

print(nw_r)
# 8
data = [10, 20, 30, 40, 50]

print(data.count(30))

print(data.index(30))

data.insert(2, 35)
print(data)

data.append(60)
print(data)

print(data)
# 9
nums = [1, 2, 3, 4, 5, 6, 7, 8]

nums = [1,2,3,4,5,6,7,8]

juftlar = sorted([n for n in nums if n % 2 == 0])
juftlar.append(10)
yigindi = sum(juftlar)

print(juftlar)
print(yigindi)
