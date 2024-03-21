from lesson_tools.tools_3 import getItems,Items 
#另一種package型式，採用資料夾方式呼叫資料

def main():
    items:Items = getItems()
    items.showAll()

main()