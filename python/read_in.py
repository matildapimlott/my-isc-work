#1
print('First Section')

with open ('weather.csv','r') as reader:
    data = reader.read()

print(data)

#2

print('Second Section')

with open ('weather.csv','r') as reader:
    line = reader.readline()
    while line != '' :
        print(line)
        line = reader.readline()

#3

print('Third Section')

rain_list=[]

with open ('weather.csv','r') as reader:
    header = reader.readline()
    for line in reader.readlines():
        rain = line.strip()
        rain = rain.split(',')
        #or rain = line.strip().split(',')
        rain = rain[-1]
        rain = float(rain)
        rain_list.append(rain)
        print(rain)

print(rain_list)

with open ('myrain.txt','w') as writer:
    for r in rain_list:
        writer.write(str(r) + ' ')





