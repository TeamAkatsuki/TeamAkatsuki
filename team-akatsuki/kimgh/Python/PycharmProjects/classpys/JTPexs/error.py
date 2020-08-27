try:
    b = [1,2]
    print(b[8])
    a = 3/0

except IndexError as f:
    print(f)
except ZeroDivisionError as e:
    print(e)
print("end")