





class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))  # Pair jobs and sort by difficulty
        worker.sort()  # Sort the workers by their abilities
    
        max_profit = 0
        best_profit = 0
        job_index = 0
        n = len(jobs)
        
        for ability in worker:
            # Move the job index to find the best job the worker can do
            while job_index < n and ability >= jobs[job_index][0]:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            max_profit += best_profit
    
        return max_profit
        