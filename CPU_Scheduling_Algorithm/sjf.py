class SJF:
    def __init__(self):
        self.pcb = []
        self.working_pcb = []
        self.counter = 0
        self.ready_queue = []
        self.added_process = 0
        self.add_process = []
        self.pcb_len = len(self.pcb)
    
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
            self.pcb_len += 1


    def add_counter(self):
        self.counter += 1
        self.check_for_process()
    
    
    def check_for_process(self):
        for i in range(self.pcb_len):
            if self.counter >= self.pcb[i]['AT']:
                if self.pcb[i]['process_id'] not in self.add_process:
                    self.working_pcb.append(self.pcb[i].copy())
                    self.added_process += 1
                    self.add_process.append(self.pcb[i]['process_id'])

        working_pcb_len = len(self.working_pcb)
        if working_pcb_len > 1:
            self.sort(self.working_pcb, 0, working_pcb_len - 1)
            self.move_to_processing(self.working_pcb[0])
        
        elif working_pcb_len == 1:
            self.move_to_processing(self.working_pcb[0])
        
        
        elif working_pcb_len == 0:
            if self.pcb_len != self.added_process:
                self.add_counter()
            else:
                return

    def sort(self, A, lo, hi):
        if hi <= lo:
            return
        lt, gt = lo, hi
        v = A[lo]['BT']
        i = lo
        while (i <= gt):
            if A[i]['BT'] < v:
                A[i], A[lt] = A[lt], A[i]
                i = i + 1
                lt = lt + 1
            elif A[i]['BT'] > v:
                A[i], A[gt] = A[gt], A[i]
                gt = gt - 1
            else:
                i = i + 1
        
        self.sort(A, lo, lt - 1)
        self.sort(A, gt+1, hi)


    def move_to_processing(self, process):
        self.ready_queue.append(process['process_id'])
        if process['BT'] == 1:
            process['BT'] -= 1
            self.counter += 1
            self.working_pcb.pop(0)
            for i in range(self.pcb_len):
                if self.pcb[i]['process_id'] == process['process_id']:
                    self.pcb[i]['CT'] = self.counter
                    self.pcb[i]['TAT'] = self.pcb[i]['CT'] - self.pcb[i]['AT']
                    self.pcb[i]['WT'] = self.pcb[i]['TAT'] - self.pcb[i]['BT']
        else:
            process['BT'] -= 1
            self.counter += 1

        if self.pcb_len != self.added_process:
            self.check_for_process()
        else:
            if self.working_pcb != []:
                self.move_to_processing(self.working_pcb[0])
            else:
                return

    
    def get_avg(self):
        wait_avg = 0
        turnaround_avg = 0
        total = 0
        for i in range(self.pcb_len):
            wait_avg += self.pcb[i]['WT']
            turnaround_avg += self.pcb[i]['TAT']
            total += 1
        
        wait_avg = wait_avg / total
        turnaround_avg = turnaround_avg / total
        print('Average waiting time: {:.2f}'.format(wait_avg))
        print('Average turnaround time: {:.2f}'.format(turnaround_avg))


    def print_data(self):
        print('{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Process', 'Arrival Time', 'Burst Time', 'Completion Time', 'Turnaround Time', 'Waiting Time'))
        for i in range(self.pcb_len):
            print('{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}'.format(self.pcb[i]['process_id'], self.pcb[i]['AT'], self.pcb[i]['BT'], self.pcb[i]['CT'], self.pcb[i]['TAT'], self.pcb[i]['WT']))    

    def get_execution_sequence(self):
        print('Execution sequence: ', end='')
        for i in self.ready_queue:
            print(i + ' -> ', end='')
   
    def run(self):
        self.get_input()
        self.check_for_process()
        self.print_data()
        self.get_avg()
        self.get_execution_sequence()
        

    
        
sjf = SJF()

if __name__ == '__main__':
    sjf.run()