def main():
        item=input("Item (enter \"done\" when finished): ")
        rec=[]
        while(not(item =="done")):
                d={}
                
                d["name"]=item
                
                price=float(input("Price: "))
                d["price"]=price
                quantity=int(input("Quantity: "))
                d["quantity"]=quantity
                rec.append(d)
                item=input("Item (enter \"done\" when finished): ")
                
        total=0
        for i in rec:
                item_price=i["price"]*i["quantity"]
                print(i["quantity"],i["name"],"%sKD"%(format(item_price,".3f")))
                
                total=total+item_price
        print("Total Price: ",total)

if __name__ == '__main__':
	main()
