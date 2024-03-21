from tools_0 import getItems,Items 
#自訂的Model執行方式，現在另一個檔案完成其內容資料，最後採用自訂Model來簡易執行輸出

def main():
    items:Items = getItems()
    items.showAll()

main()