def f123():
    for hello in range(2):
        yield 2 + hello
        yield 3 + hello


for i in f123():
    print(i)

