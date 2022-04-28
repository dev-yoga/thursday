mango_batches = [2, 4, 6, 8, 10, 12, 14, 16]
mangoes_added = [num + 2 for num in mango_batches]

print(mangoes_added)

enough_mangoes = [mango for mango in mango_batches if mango > 10]
print(enough_mangoes)