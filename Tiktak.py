
from multiprocessing import Process,current_process

def square(number):
    process_name=current_process().name
    print(f"{process_name} calculate the square of {number}")
    result=number*number
    print(f"{process_name} result={result}")
if __name__=="__main__":
    list_number=[1,2,3,4,5]
    list_process=[]
    for num in list_number:
        process_of=Process(target=square,args=(num,)) #beacuse the tuple get one item use ,
        list_process.append(process_of)

    for process_in in list_process:
        process_in.start()

    for process_in in list_process:
        process_in.join()
