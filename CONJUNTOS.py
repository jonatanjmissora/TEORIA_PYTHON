odd = set([1, 3, 5, 7, 9])
even = set([2, 4, 6, 8, 10])
print(odd.union(even))          # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(odd.intersection(even))   # set()

a = [1, 1, 2, 3, 3, 4, 5, 5]
b = list(set(a))                # b = [1, 2, 3, 4, 5]
print(b)

# otra con lista comprimida
b = []
[b.append(i) for i in a if i not in b]
print(b)

#otra
c = []
c.extend(i for i in a if i not in c)
print(c)
