import timestart = time.time()

L = [i for i in range (1, 100000000) if i%3 == 0]

end = time.time()

print(float(end)-float(start))

# 5.0334999561309814 seconds
