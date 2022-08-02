def pre_process(file_name):
    data = []
    with open(file_name) as f:
        data = f.readlines()
    f.close()
    
    data = [x.strip() for x in data]


    index  = 0
    
    while not(data[index].endswith("*/") and data[index+1].startswith('struct')):
        index+=1


    with open('headers.txt','a') as f:
        for i in range(len(data)):
            if i >= index:
                f.write(data[i]+'\n')
    f.close()


def vaild(s:str):
    return '__gnu_cxx' not in s and 'std::' not in s and 'leveldb::' not in s and 'entt::' not in s and 'JsonUtil::' not in s and 'google::' not in s and 'grpc_core::' not in s and 'Json::' not in s and 'gsl::' not in s and 'grpc::' not in s
def to_typedef_markdown(item: list[str]):
    return '#### ' + item[1] + '\n\n'
    

def to_enum_markdown(item: list[str]):
    s = '#### ' + item[1][5:] + '\n'
    s += '```cpp\n'
    for x in item:
        s += x+'\n'
    s +='\n```\n'
    return s

def to_struct_markdown(item: list[str]):
    s = '#### ' + item[1][7:] + '\n'
    s += '```cpp\n'
    for x in item:
        s += x+'\n'
    s +='\n```\n'
    return s



def write_item_list(items,t, name):
    items.sort(key=lambda x: x[1])
    with open(name,'a') as f:
        for item in items:
            if t == 'enum':
                f.write(to_enum_markdown(item))
            elif t == 'type':
                f.write(to_typedef_markdown(item))
            elif t =='struct':
                f.write(to_struct_markdown(item))
        f.close()


def process_header(file_name):    
    data= []
    with open(file_name) as f:
        data = f.readlines()
    f.close()

    item = []
    item_list = []
    for line in data:
        line = line.strip()
        if len(line) == 0:
            item_list.append(item)
            item = []
        else:
            item.append(line)


    typedefs  = []
    enums = []
    structs = {}
    for item in item_list:
        if len(item) > 1 and vaild(item[1]):
            name = item[1]
            if name.startswith('struct'):
                k = name[7]
                if k not in structs:
                    structs[k] = []
                else:
                    structs[k].append(item)

            elif name.startswith('typedef'):
                typedefs.append(item)
            elif name.startswith('enum'):
                enums.append(item)


    index = ''
    index += '# Index\n'
    index += '## Structs\n'

    ss = []

    out = '../src/'
    for key, value in structs.items():
        if key == '`':
            key = 'backtick'
        if key.isalpha():
            if key.islower():
                na = 'struct'+'Lower'+key.upper();
            elif key.isupper():
                na = 'struct'+'Upper'+key.upper();
        else:
            na = 'struct'+key
        ss.append('- [`%s`](%s)\n' % (key,na+'.html'))
        write_item_list(value,'struct',out + '/'+na+'.md')
    ss.sort()
    for x in ss:
        index += x
    index += '## Others\n'
    index += '- [Enums](enums.html)\n'
    index += '- [Typedefs](typedefs.html)\n'
    write_item_list(enums,'enum',out+'/enums.md')
    write_item_list(typedefs,'type',out+'/typedefs.md')

    with open(out + '/index.md','a') as f:
        f.write(index)
        f.close()


if __name__ == "__main__":
    process_header('headers.txt')

 

