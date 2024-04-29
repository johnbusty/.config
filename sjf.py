# Python code equivalent to the provided Java code

def waiting_time(n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def turnaround_time(n, bt, wt, tt):
    for i in range(n):
        tt[i] = bt[i] + wt[i]

def avg_wt_tt(n, bt):
    wt = [0] * n
    tt = [0] * n
    waiting_time(n, bt, wt)
    turnaround_time(n, bt, wt, tt)
    
    print("\nProcesses || Burst Time || Arrival Time || Waiting Time || Turn-Around Time ")
    awt = 0
    att = 0
    for i in range(n):
        awt += wt[i]
        att += tt[i]
        print(f"{i + 1}\t ||\t{bt[i]}\t||\t{wt[i]}\t||\t{tt[i]}")
    
    awt /= n
    att /= n
    print("\nAverage waiting time = ", awt)
    print("\nAverage turn around time = ", att)

# Main function
def main():
    n = int(input("Enter the number of processes: "))
    bt = [0] * 20
    print("\nEnter the Burst Time for each process.")
    for i in range(n):
        bt[i] = int(input(f"\nFor Process {i + 1}:"))
    avg_wt_tt(n, bt)

if __name__ == "__main__":
    main()
