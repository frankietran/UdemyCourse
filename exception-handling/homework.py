car = {"make": "", "model": "", "year": 0}
try:
    print(car["color"])
except:
    print("Never created the color key")
finally:
    print("Finally always executed")
