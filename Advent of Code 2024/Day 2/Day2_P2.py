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


def is_safe(report):
    if len(report) < 2:
        return True
    
    order = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
        
        if order is None:
            if diff > 0:
                order = 1  # Increasing
            elif diff < 0:
                order = -1  # Decreasing
        else:
            if (order == 1 and diff < 0) or (order == -1 and diff > 0):
                return False
            
    return True


def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
        
    return False


if __name__ == "__main__":
    safe_reports = 0

    while True:
        try:
            report = init()
            if is_safe_with_dampener(report):
                safe_reports += 1
        except EOFError:
            break
    
    print(safe_reports)

    