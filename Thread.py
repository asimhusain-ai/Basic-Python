import threading
def cube(x):
    print("Cube :- {}".format(x*x*x))
def square(x):
    print("Square :- {}".format(x*x))
if __name__=="__main__":
    t1 = threading.Thread(target=cube,args=(5,))
    t2 = threading.Thread(target=square,args=(6,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()