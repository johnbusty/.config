import sys

n, i, qt, count, temp, sq = 0, 0, 0, 0, 0, 0
bt, wt, tat, rem_bt = [0] * 10, [0] * 10, [0] * 10, [0] * 10
awt, atat = 0, 0

print("Enter the number of process = ")
n = int(input())
print("Enter the burst time of the process")
for i in range(n):
    print("P" + str(i) + " = ")
    bt[i] = int(input())
    rem_bt[i] = bt[i]

print("Enter the quantum time: ")
qt = int(input())

while True:
    for i in range(n):
        temp = qt
        if rem_bt[i] == 0:
            count += 1
            continue
        if rem_bt[i] > qt:
            rem_bt[i] -= qt
        elif rem_bt[i] >= 0:
            temp = rem_bt[i]
            rem_bt[i] = 0
        sq += temp
        tat[i] = sq
    if n == count:
        break

print("\nProcess Burst Time Turnaround Time Waiting Time\n")
for i in range(n):
    wt[i] = tat[i] - bt[i]
    awt += wt[i]
    atat += tat[i]
    print("\n " + str(i + 1) + "\t\t " + str(bt[i]) + "\t\t " + str(tat[i]) + "\t\t " + str(wt[i]) + "\n")

awt /= n
atat /= n
print("\nAverage waiting Time = " + str(awt) + "\n")
print("Average turnaround time = " + str(atat))
