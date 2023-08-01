#Koo susan
#TP067306

def supplier_registration():
    while True:
        fh = open ("suppliers.txt","w")
        supplier_list = []
        spl = 0
        while spl < 3:
            supcode = input("Please enter supplier code: ")
            supname = input("Please enter supplier name: ")
            supitems = input("Please enter supplier contact number: ")
            supadd = input("Please enter supplier address: ")
            print()
            spl += 1
            suprec = supcode+","+supname+","+supitems+","+supadd
            supplier_list.append(str(suprec))
            fh.write(suprec+"\n")
            
        while spl == 3:
            choice = int(input("Do you want to enter fourth supplier details? [1-yes, 0-no]: "))
            if (choice == 1):
                supcode = input("Please enter supplier code: ")
                supname = input("Please enter supplier name: ")
                supitems = input("Please enter supplier contct number: ")
                supadd = input("Please enter supplier address: ")
                suprec4 = supcode+","+supname+","+supitems+","+supadd
                supplier_list.append(str(suprec4))
                fh.write(suprec4+"\n")
                fh.close()
                menu()
            if (choice == 0):
                fh.close()
                print("Thank you have a nice day!")
                menu()


def save_supplier_reg_list():
    try:
        fileHandler = open('suppliers.txt','w')
    except:
        print('File cannot be opened: ')
        exit()
    supplier_list = supplier_registration()

    for spl in supplier_list:
        for sl in spl:
            fileHandler.write(sl)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

def print_supplier_reg_list():
    try:
        fileHandler = open('suppliers.txt', 'r')
    except:
        print('File cannot be opened')
        exit()

    for line in fileHandler:
        line=line.rstrip()
        print(line)
    fileHandler.close()

def save_item_detials():
    try:
        fileHandler = open('ppe.txt','w')
    except:
        print('File cannot be opened')
        exit()

    for line in fileHandler:
        fileHandler.write()
        fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()
    
def hospital_registration():
    print('All the hospital details will be overwritten')
    while True:
        fh = open ("hospitals.txt","w")
        hospital_list = []
        hsp = 0
        while hsp < 3:
            hospital_code = input("Please enter hospital code: ")
            hospital_pn = input("Please enter hospital contact number: ")
            hapital_address= input("Please enter hospital address: ")
            print()
            hsp += 1
            hspreg = hospital_code+","+hospital_pn+","+hapital_address
            hospital_list.append(str(hspreg))
            fh.write(hspreg+"\n")
            
        while hsp == 3:
            choice = int(input("Do you want to enter fourth hospital details? [1-yes, 0-no]: "))
            if (choice == 1):
                hospital_code = input("Please enter hospital code: ")
                hospital_pn = input("Please enter hospital contact number: ")
                hospital_address = input("Please enter hospital address: ")
                hspreg4 = hospital_code+","+hospital_pn+","+hapital_address
                hospital_list.append(str(hspreg4))
                fh.write(hspreg4+"\n")
                fh.close()
                menu()
            if (choice == 0):
                fh.close()
                print("Thank you have a nice day!")
                menu()
            else:
                print('Invalid input')



def print_item_supplier():
    fileHandler = open('ppe.txt','r')
    for line in fileHandler:
        print(line)
    fileHandler.close()


def save_hospital_reg_list():
    fileHandler = open ('hospitals.txt','w')
    hospital_list = hospital_registration()

    for hptl in hospital_list:
        for hp in hptl:
            fileHandler.write(hp)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

def print_hospital_reg_list():
    fileHandler = open('hospitals.txt','r')

    for line in fileHandler:
        line = line.rstrip()
        print(line)
    fileHandler.close()

def openning_ppe():
    fileHandler = open('ppe.txt','w')
    fileHandler.write("Item code"+"-"+"Item name"+"-"+"Item Quantity"+"-"+"Supplier code")
    fileHandler.write('\t')
    fileHandler.write('\n')
    fileHandler.close()

#check
def checkItemCodeIsAssigned (item_code):

    fileHandler = open('ppe.txt','r')
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        if (lines [0] == item_code):
            return True
    return False

  
def assign_Item_to_supplier():
    item_code = input('Pls Insert Your Item Code: ')
    itemAssignedToSupplier  = checkItemCodeIsAssigned(item_code)
    
    if (itemAssignedToSupplier == True):
        print()
        print('This item is taken by another supplier')
    else:
        supplier_code = input('You want to assign this item to which supplier (Enter the supplier code): ')
        item_name = input('Pls Enter Item name: ')
        custom_quantity = int(input('Do you want to set 100 boxes(default quantity) as the item quantity? [1-yes, 0-No]' ))
        if(custom_quantity == 1):
            item_quantity = 100
        else:
            item_quantity = int(input('Pls Enter Item Quantity in boxes: '))

        fileHandler = open('ppe.txt','a+')
        fileHandler.write(item_code + "," + item_name + "," + str(item_quantity)+ "," + supplier_code)
        fileHandler.write('\n')
        fileHandler.close()

        while True:
            print()
            cont = int(input('Want to assign another item? [1-yes, 0-No and Exit]: '))
            if (cont == 1):
                assign_Item_to_supplier()
            else:
                break

def checkQuantity(quantity,item_code):

    fileHandler = open('ppe.txt','r')
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        if(int(lines[2]) < int(quantity)):
           return False,lines[2]
        else:
           return True,lines[2]
    return False,0

def check_supplier_code(supplier_code_re):

    fileHandler = open('ppe.txt','r')
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        if (lines[3] == supplier_code_re):
            return True
    return False

def receive_item_supplier():
    item_code_assign = input('Enter item code: ')
    item_code_check = checkItemCodeIsAssigned (item_code_assign)
    
    if(item_code_check == True):
        print()
        supplier_code_re = input('Item received from which supplier? Enter supplier code: ')
        supplier_code_exist  = check_supplier_code(supplier_code_re)

        if (supplier_code_exist == True):
            print()
            print('supplier code exist')
            print()
            reveiced_boxes = input ('How many boxes received? ')
            fileHandler = open ("ppe.txt",'r')

            ppe_contentss = []

            for lines in fileHandler:
                lines = lines.rstrip()
                lines = lines.split(",")
                ppe_contentss.append(lines)

            for detailss in ppe_contentss:
                if detailss[0] == item_code_assign:
                    detailss[2] = int(detailss[2]) + int(reveiced_boxes)
                    print('Remaining item quantity: ',detailss[2])
                
            fileHandler = open("ppe.txt",'w')
            for detailss in ppe_contentss:
                fileHandler.write(str(detailss[0]) + "," + str(detailss[1]) + "," + str(detailss[2]) + "," + str(detailss[3]) + "\n")
            fileHandler.close()
        else:
            print()
            print("Supplier code doesn't exist, pls register this supplier")

    else:
        print("Sorry this item haven't assigned to any supplier yet, Choose option 3 to assign item first! ")

        
def distribute_item_to_hospital():
    item_code_to_dis = input('Pls enter item code: ')
    item_quantity_to_dis = int(input('How many boxes u want to distribute: '))
    select_hosp = input ('Which hospital? Pls enter the hospital code: ')
                               
    can_distribute_to_hos, remaining_stock = checkQuantity(item_quantity_to_dis,item_code_to_dis)

    if(can_distribute_to_hos):
        print()
        print('Successful')
        fileHandler = open("ppe.txt",'r')
        
        ppe_contents = []

        for lines in fileHandler:
            lines = lines.rstrip()
            lines = lines.split(",")
            ppe_contents.append(lines)

        for details in ppe_contents:
            if details[0] == item_code_to_dis:
                details[2] = int(details[2]) - item_quantity_to_dis
                print()
                print('Remaining item quantity: ',details[2])
                
        fileHandler = open("ppe.txt",'w')
        for details in ppe_contents:
            fileHandler.write(str(details[0]) + "," + str(details[1]) + "," + str(details[2]) + "," + str(details[3]) + "\n")
        fileHandler.close()

        fileHandler = open('distribution.txt','a')
        fileHandler.write(item_code_to_dis + "," + select_hosp + "," + str(item_quantity_to_dis) + "\n")
        fileHandler.close()
                
    else:
        print("Can't distribute! Item quantity insufficient,sorry!")
        

def save_distribute_details():
    try:
        fileHandler = open('distribution.txt','w')
    except:
        print('File cannot be opened')
        exit()

    for line in fileHandler:
        fileHandler.write()
        fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()


def sort_item_list(ppe_contents):
    
    sort_list = len(ppe_contents)
    for i in range(sort_list):
        for s in range(sort_list - i - 1):
            if ppe_contents[s][0] > ppe_contents [s + 1][0]:
                init = ppe_contents[s]
                ppe_contents[s] = ppe_contents[s + 1]
                ppe_contents[s + 1] = init
    return ppe_contents

                
def check_item_less_25():

    initemppresent = []
    
    fileHandler = open("ppe.txt",'r')
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        if int(lines[2]) < 25:
            initemppresent.append(lines)
    initemppresent = sort_item_list(initemppresent)
    print_item_less_25(initemppresent)


def print_item_less_25(printlol):

    for line in printlol:
        print('\n')
        print(line)

def view_all_details():

    initemppresent = []
    
    fileHandler = open("ppe.txt",'r')
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        initemppresent.append(lines)
        
    initemppresent = sort_item_list(initemppresent)
    print_item_less_25(initemppresent)
    
def search_item():
    fileHandler = open("distribution.txt",'r')
    searchInput = input("Type item code to search: ")

    for line in fileHandler:
        line = line.rstrip()
        if not searchInput.lower() in line.lower():
            continue
        print('\n')
        print(line)
    fileHandler.close()

    
def menu():
    while True:
        print('\n')
        print('===================Main Menu===================\n')
        print('Select the operation that you want to perform: ')
        print('1.  Supplier registration')
        print('2.  Hospital registration ')
        print('3.  Assign Item to supplier')
        print('4.  Receiving item from supplier')
        print('5.  Distribution of items' )
        print('6.  View all details')
        print('7.  Search item')
        print('8.  View item （< 25 boxes）')
        print('9.  Exit')
        print()
        choice= input('Enter selection: ')
        try:
            choice = int(choice)
            if(choice == 1):
                save_supplier_reg_list()
            elif(choice == 2):
                save_hospital_reg_list()
            elif(choice == 3):
                assign_Item_to_supplier()
            elif(choice == 4):
                receive_item_supplier()
            elif(choice == 5):
                distribute_item_to_hospital()
            elif(choice == 6):
                view_all_details()
            elif(choice == 7):
                search_item()
            elif(choice == 8):
                check_item_less_25()
            elif(choice == 9):
                print('Have a good day! Goodbye')
                break
            else:
                print('\n')
                print('Invalid input')
        except:
            print('choice must be a number, Pls try again!')
            print()
        

menu()
        
