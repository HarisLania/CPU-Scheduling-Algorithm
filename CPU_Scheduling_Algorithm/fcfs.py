class FCFS:
    def __init__(self):
        self.pcb = []
    
    def get_input(self):
        processes = int(input('Enter number of process: '))
        for i in range(processes):
            name = input('Enter process name: ')
            self.pcb.append({
                'process_id': name,
                'arrival_time': int(input('Enter arrival time of ' + name + ': ')),
                'burst_time': int(input('Enter burst time of ' + name + ': ')),
                'waiting_time': 0,
                'turnaround_time':0
            })

    
    def get_arrival_time(self):
        for i in range(len(self.pcb)):
            print(self.pcb[i]['arrival_time'])
        
    def sort(self, A, lo, hi):
        if hi <= lo:
            return
        lt, gt = lo, hi
        v = A[lo]['arrival_time']
        i = lo
        while (i <= gt):
            if A[i]['arrival_time'] < v:
                A[i], A[lt] = A[lt], A[i]
                i = i + 1
                lt = lt + 1
            elif A[i]['arrival_time'] > v:
                A[i], A[gt] = A[gt], A[i]
                gt = gt - 1
            else:
                i = i + 1
        
        self.sort(A, lo, lt - 1)
        self.sort(A, gt+1, hi)

    

    def get_waiting_time(self):
        for i in range(len(self.pcb)):
            if i == 0:
                self.pcb[i]['waiting_time'] = self.pcb[i]['arrival_time']
            else:
                if (self.pcb[i]['arrival_time'] <= self.pcb[i-1]['burst_time'] + self.pcb[i-1]['waiting_time']):
                    self.pcb[i]['waiting_time'] = self.pcb[i-1]['burst_time'] + self.pcb[i-1]['waiting_time']
                else:
                    self.pcb[i]['waiting_time'] = self.pcb[i]['arrival_time']
        

    def get_arrival_time(self):
        # TAT = arrival_time + WT
        for i in range(len(self.pcb)):
            self.pcb[i]['turnaround_time'] = self.pcb[i]['burst_time'] + self.pcb[i]['waiting_time']
    
    
    def get_avg(self):
        wait_avg = 0
        turnaround_avg = 0
        total = 0
        for i in range(len(self.pcb)):
            wait_avg += self.pcb[i]['waiting_time']
            turnaround_avg += self.pcb[i]['turnaround_time']
            total += 1
        
        wait_avg = wait_avg / total
        turnaround_avg = turnaround_avg / total
        print('Average waiting time: {:.2f}'.format(wait_avg))
        print('Average turnaround time: {:.2f}'.format(turnaround_avg))


    def print_data(self):
        print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Process', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turnaround Time'))
        for i in range(len(self.pcb)):
            print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(self.pcb[i]['process_id'], self.pcb[i]['arrival_time'], self.pcb[i]['burst_time'], self.pcb[i]['waiting_time'], self.pcb[i]['turnaround_time']))


    def run(self):
        self.get_input()
        self.sort(self.pcb, 0, len(self.pcb)-1)
        self.get_waiting_time()
        self.get_arrival_time()
        self.print_data()
        self.get_avg()

fcfs = FCFS()
fcfs.run()




