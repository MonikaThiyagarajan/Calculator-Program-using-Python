import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="calculator")
cur = con.cursor(buffered=True)



def add():
    b = int(input("Enter the first number : "))
    c = int(input("Enter the second number : "))
    d = b + c
    print(d)
    import datetime
    now = datetime.datetime.now()
    e = now.strftime("%H:%M:%S")
    cur.execute("""INSERT INTO calc(Addition, Times) values (\"""" + str(d) + """\",\"""" + e + """\")""")
    con.commit()
    main()

def sub():
    b = int(input("enter the first number : "))
    c = int(input("enter the second number : "))
    d = b - c
    print(d)
    import datetime
    now = datetime.datetime.now()
    e = now.strftime("%H:%M:%S")
    cur.execute("""INSERT INTO calc(Subtraction, Times) values (\"""" + str(d) + """\",\"""" + e + """\")""")
    con.commit()
    main()

def mul():
    b = int(input("enter the first number : "))
    c = int(input("enter the second number : "))
    d = b * c
    print(d)
    import datetime
    now = datetime.datetime.now()
    e = now.strftime("%H:%M:%S")
    cur.execute("""INSERT INTO calc(Multiplication, Times) values (\"""" + str(d) + """\",\"""" + e + """\")""")
    con.commit()
    main()

def div():
    b = int(input("enter the first number : "))
    c = int(input("enter the second number : "))
    d = b / c
    print(d)
    import datetime
    now = datetime.datetime.now()
    e = now.strftime("%H:%M:%S")
    cur.execute("""INSERT INTO calc(Division, Times) values (\"""" + str(d) + """\",\"""" + e + """\")""")
    con.commit()
    main()

print("1. press 1 for addition""\n""2. press 2 for subraction""\n""3. press 3 for multiplication""\n""4. press 4 for division""\n""5. press 5 for exit")
def main():
    a = int(input("Enter the number : "))
    while(True):
        if a == 5:
            print("see you, come again!!")
            quit()
        elif a == 1:
            add()
        elif a == 2:
            sub()
        elif a == 3:
            mul()
        elif a == 4:
            div()
        else:
            break
main()