x = "Pero que luz se deja ver allí"
palabras = x.split()
t = list()
for palabra in palabras:
    t.append((len(palabra), palabra))
t.sort(reverse=True)
print(t)

res = list()
for longitud, palabra in t:
    res.append(palabra)

print(res)
