print("""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
""")
i=1
for i in range(101):
    if(i%3 != 0):
        continue
    else:
        print(i)