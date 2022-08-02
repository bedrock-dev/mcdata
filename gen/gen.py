import os
import markdown
import sys


def get_style(paths: list[str]):
    res = ''
    for path in paths:
        res += '<link rel="stylesheet" type="text/css" href="%s">\n' % path
    return res 


def read_file(name:str):
    text = ''
    with open(name, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text

def	write_file(path:str,conetent :str):
	with open(path, 'w',encoding='utf-8') as f:
 	   f.write(conetent)

    
def generate_html(input_makrdown:str,style):
    md = markdown.Markdown(extensions = ['nl2br','meta','extra','codehilite','md4mathjax'])
    content = md.convert(input_makrdown)
    template = read_file('template.html')

    time_meta = md.Meta.get('date')
    time = ''
    if time_meta is not None:
        time = time_meta[0]

    title_meta = md.Meta.get('title')
    title = "MCData"
    if time_meta is not None:
        title = title_meta[0]

    return template % (get_style(style) ,title ,content),time
    


def cmp(a,b):
    ta = a['time']
    tb = b['time']
    if ta > tb:
        return -1
    elif ta < tb:
        return 1
    return 0

def process(input_path:str,output_path:str):
    all_files =  os.listdir(input_path)
    markdown_files = [x for x in all_files if x.endswith('.md')]
    indexes = []
    csses = ['styles.css','custom.css']
    for file in markdown_files:
        name = file[:-3]
        markdown_path = input_path +'/'+file
        print(markdown_path)
        html,time = generate_html(read_file(markdown_path),['./style/' + x for x in csses])
        write_file(output_path+'/'+name+'.html',html)
        indexes.append({'time':time,'name': name })
    
if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("use py gen.py [input folder] [output folder]")
        exit(-1)
    #path = 'D:/blog/source/_posts'
    #output = './outputs'
    process(sys.argv[1],sys.argv[2])
