import heapq

def assign_jobs_equal_machines(jobs, m):
    machines = [0] * m
    # Sắp xếp công việc theo thời gian giảm dần
    jobs.sort(reverse=True)

    for job in jobs:
        # Đưa công việc vào máy có tổng thời gian hiện tại thấp nhất
        min_machine = heapq.heappop(machines)
        min_machine += job
        heapq.heappush(machines, min_machine)

    # Thời gian hoàn tất công việc là thời gian của máy có tổng lớn nhất
    return max(machines)

# Danh sách công việc và số máy
jobs = [5, 2, 3, 7, 1, 4]
m = 3
min_completion_time = assign_jobs_equal_machines(jobs, m)
print(f"Thời gian hoàn tất công việc (công suất máy bằng nhau): {min_completion_time}")
