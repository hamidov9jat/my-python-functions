 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius)




celsius_dict = \
{tx: degree for (tx, degree) in zip(fahrenheit.keys(), 
    map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))}

print(celsius_dict)


print("----------------------------------")
nested_dict = {'first':{'a':1}, 'second':{'b':2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)
print("----------------------------------")

nested_dict = {'first':{'a':1}, 'second':{'b':2}}

for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})

print((outer_k, outer_v))
# nested_dict.update({outer_k:outer_v})

print(nested_dict)



