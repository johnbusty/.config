def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    for i in range(len(process_size)):
        wst_idx = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if wst_idx == -1:
                    wst_idx = j
                elif block_size[wst_idx] < block_size[j]:
                    wst_idx = j
        if wst_idx != -1:
            allocation[i] = wst_idx
            block_size[wst_idx] -= process_size[i]
    
    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(len(process_size)):
        print(f" {i + 1}\t\t{process_size[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

block_size = [100, 500, 200, 300, 600]
process_size = [212, 417, 112, 426]
worst_fit(block_size, process_size)
