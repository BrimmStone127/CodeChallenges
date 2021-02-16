'''
Given the following log file structure:

2020-09-29T01:59:14.214Z key5=15,key4=11,hello=1
2020-09-29T02:00:31.011Z key3=22,key4=33,key5=16

Sum the values by key. So the expected result is: 

hello=1
key3=22
key4=44
key5=31
'''
log_arr = ["2020-09-29T01:59:14.214Z key5=15,key4=11,hello=1", "2020-09-29T02:00:31.011Z key3=22,key4=33,key5=16"]
unique_keys = {}

for x in log_arr:
    key = x.split(" ")
    info = key[1]
    keys = info.split(",")

    for y in keys:
        entry = y.split("=")
        key_name = entry[0]
        key_value = entry[1]

        if key_name in unique_keys:
            unique_keys[key_name] += int(key_value)
        if key_name not in unique_keys:
            unique_keys[key_name] = int(key_value)

print(unique_keys)