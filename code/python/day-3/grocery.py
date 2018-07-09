import json
def send_data(gfile):
     data = json.dumps(gfile)
     f=open("file.json","a+")
     f.write(data)
     f.close()

def search(name):
    glist = json.load(open('file.json'))
    print(glist(name))

num = int(input("Enter the number of items to store or press '0' => "))
item_list={}

if num!=0:
    for i in range(1,num+1):
        name = input("Enter the name of item=> ")
        quantity = input("Enter the quantity to store=> ")
        item_list[name] = quantity
        send_data(item_list)

find = input("Enter the item to search=> ")
search(find)
