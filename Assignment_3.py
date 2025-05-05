# Job Scheduling Problem
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling():
    n = int(input("\nEnter number of jobs: "))
    jobs = []

    for _ in range(n):
        job_id = input("Enter job ID: ")
        deadline = int(input(f"Enter deadline for job {job_id}: "))
        profit = int(input(f"Enter profit for job {job_id}: "))
        jobs.append(Job(job_id, deadline, profit))

    # Sort jobs by descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    slots = [False] * max_deadline
    job_order = [None] * max_deadline

    total_profit = 0

    for job in jobs:
        for i in range(min(job.deadline, max_deadline) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                job_order[i] = job.job_id
                total_profit += job.profit
                break

    print("\nScheduled Jobs:", [job for job in job_order if job])
    print("Total Profit:", total_profit)

# Selection Sort
def selection_sort():
    n = int(input("\nHow many numbers to sort? "))
    nums = []

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    print("Sorted numbers:", nums)

# Menu
while True:
    print("\nMenu:")
    print("1. Job Scheduling")
    print("2. Selection Sort")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        job_scheduling()
    elif choice == '2':
        selection_sort()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
