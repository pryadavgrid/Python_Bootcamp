try:
    f = open("file.txt",'r')
except Exception as e:
    print(f"Error is : {e}")
else:
    # f.write("This Is Testing File\nOK")
    content = f.read()
    print(content)
finally:
    print("Done !!")
    try :
        f.close()
    except:
        pass