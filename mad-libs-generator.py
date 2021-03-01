import random

mad_libs = [
    {
        "lib_string": "What came first the chicken on the %s ?",
        "input_types": ['noun']
    },
    {
        "lib_string": "Be careful when you vaccum the %s when you clean under the %s bed",
        "input_types": ['noun', 'adjective']
    },
    {
        "lib_string": "I like my doughnuts with extra %s on them",
        "input_types": ['noun']
    },
    {
        "lib_string": "Once that %s music starts playing, its time to stop the acceptance speech",
        "input_types": ['adjective']
    }
]

def main():
    input_vals = []
    madlib = mad_libs[random.randint(0, len(mad_libs) - 1)]
    for input_type in madlib["input_types"]:
        print("Enter a %s" % input_type)
        input_val = input()
        input_vals.append(input_val)
    val_tuple = tuple(input_vals)
    print(madlib['lib_string'] % val_tuple)

if __name__ == '__main__':
    main()