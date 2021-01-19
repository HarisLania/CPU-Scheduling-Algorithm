class RoundRobin:
    def __init__(self, quantum_time):
        self.quantum_time = quantum_time
        self.pcb = []
        self.working_pcb = []
        self.counter = 0
        self.ready_queue = []
        self.waiting_queue = []
        self.added_process = []
        self.all_zeros = True
    
    def get_input(self):
        processes = int(input('Enter number of process: '))
        for i in range(processes):
            name = input('Enter process name: ')
            self.pcb.append({
                'process_id': name,
                'AT': int(input('Enter arrival time of ' + name + ': ')),
                'BT': int(input('Enter burst time of ' + name + ': ')),
                'WT': 0,
                'TAT':0,
                'CT':0,
            })


    def add_counter(self):
        self.counter += 1
        self.check_for_process(0)
    
    
    def check_for_process(self, start):
        process_len = 0
        if len(self.pcb) == len(self.added_process):
            if self.working_pcb == [] and self.waiting_queue == []:
                return

        for i in range(len(self.pcb)):
            if self.counter >= self.pcb[i]['AT']:
                if self.pcb[i]['process_id'] not in self.added_process:
                    self.working_pcb.append(self.pcb[i].copy())
                    self.added_process.append(self.pcb[i]['process_id'])
                    process_len += 1
                    if self.pcb[i]['AT'] == 0 and self.all_zeros == True:
                        self.all_zeros = True
                    else:
                        self.all_zeros = False

        if process_len > 1:
            if self.all_zeros == False:
                self.sort(self.working_pcb, 0, process_len - 1)
            
            self.move_to_processing(self.working_pcb[0])
        
        elif process_len == 1:
            self.move_to_processing(self.working_pcb[0])
        
        elif process_len == 0:
            if self.waiting_queue != []:
                self.working_pcb.append(self.waiting_queue[0])
                self.waiting_queue.pop(0)
                self.move_to_processing(self.working_pcb[0])
            else:
                if self.working_pcb != []:
                    self.move_to_processing(self.working_pcb[0])
                else:
                    self.add_counter()

    def sort(self, A, lo, hi):
        if hi <= lo:
            return
        lt, gt = lo, hi
        v = A[lo]['AT']
        i = lo
        while (i <= gt):
            if A[i]['AT'] < v:
                A[i], A[lt] = A[lt], A[i]
                i = i + 1
                lt = lt + 1
            elif A[i]['AT'] > v:
                A[i], A[gt] = A[gt], A[i]
                gt = gt - 1
            else:
                i = i + 1
        
        self.sort(A, lo, lt - 1)
        self.sort(A, gt+1, hi)


    def move_to_processing(self, process):
        self.ready_queue.append(process['process_id'])
        if process['BT'] <= self.quantum_time:
            self.counter += process['BT']
            process['BT'] = 0
            self.working_pcb.pop(0)
            for i in range(len(self.pcb)):
                if self.pcb[i]['process_id'] == process['process_id']:
                    self.pcb[i]['CT'] = self.counter
                    self.pcb[i]['TAT'] = self.pcb[i]['CT'] - self.pcb[i]['AT']
                    self.pcb[i]['WT'] = self.pcb[i]['TAT'] - self.pcb[i]['BT']
            if len(self.waiting_queue) >= 1:
                self.working_pcb.append(self.waiting_queue[0])
                self.waiting_queue.pop(0)
                self.check_for_process(len(self.working_pcb))
            else:
                self.check_for_process(0)
        
        else:
            self.counter += self.quantum_time
            process['BT'] -= self.quantum_time
            self.waiting_queue.append(process)
            self.working_pcb.pop(0)
            if len(self.waiting_queue) > 1:
                self.working_pcb.append(self.waiting_queue[0])
                self.waiting_queue.pop(0)
                self.check_for_process(1)
            else:
                self.check_for_process(0)

    
    def get_avg(self):
        wait_avg = 0
        turnaround_avg = 0
        total = 0
        for i in range(len(self.pcb)):
            wait_avg += self.pcb[i]['WT']
            turnaround_avg += self.pcb[i]['TAT']
            total += 1
        
        wait_avg = wait_avg / total
        turnaround_avg = turnaround_avg / total
        print('Average waiting time: {:.2f}'.format(wait_avg))
        print('Average turnaround time: {:.2f}'.format(turnaround_avg))


    def print_data(self):
        print('{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Process', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turnaround Time', 'Completion Time'))
        for i in range(len(self.pcb)):
            print('{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}'.format(self.pcb[i]['process_id'], self.pcb[i]['AT'], self.pcb[i]['BT'], self.pcb[i]['WT'], self.pcb[i]['TAT'], self.pcb[i]['CT']))    

    def get_execution_sequence(self):
        print('Execution sequence: ', end='')
        for i in self.ready_queue:
            print(i + ' -> ', end='')
   
    def run(self):
        self.get_input()
        self.check_for_process(0)
        self.print_data()
        self.get_avg()
        self.get_execution_sequence()
        

    
        
        



round_robin = RoundRobin(int(input('Enter quantum time: ')))
round_robin.run()


