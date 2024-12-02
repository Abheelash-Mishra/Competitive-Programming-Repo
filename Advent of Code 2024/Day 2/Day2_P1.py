################ ---- Input Functions ---- ################

def inp():
    return(int(input()))
def inst():
    return(list(map(str,input().split())))
def init():
    return(list(map(int,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    safe_reports = 0

    while True:
        try:
            report = init()

            order = 0           # 1: ascending, -1: descending
            if report[0] < report[1]:
                order = 1
            elif report[0] > report[1]:
                order = -1
            
            if order == 0:
                continue
            
            broke = False
            for i in range(len(report)-1):
                if order == 1:
                    if report[i] > report[i+1] or abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
                        broke = True
                        break
                elif order == -1:
                    if report[i] < report[i+1] or abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
                        broke = True
                        break
            
            if not broke:
                safe_reports += 1
        
        except:
            break
    
    print(safe_reports)
    