def input_name():
    name_list=[]
    
    while(True):
        name = input("Enter a name to list('quit' to stop): ")
        if name == "quit":
            break
        name_list.append(name)
    return name_list

def name_list():
    name_list = input_name()
    
    len_dict=dict()
    for name in name_list:
        if len(name) not in len_dict:
            len_dict[len(name)] = [name]
        else:
            len_dict[len(name)].append(name)
    print(len_dict)
    return len_dict
    
    
def main():
    name_list()

if __name__ == "__main__":
    main()
    