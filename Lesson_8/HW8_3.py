class InvData(Exception):

    def __init__(self, text):
        self.text = text


class SuperDuper:
    ans = []

    def __init__(self):
        self.t_next = input('Enter next line (numbers) or "stop" to exit: ')
        self.text = self.t_next.strip().split()
        self.check_data()

    def check_data(self):
        for i in self.text:
            try:
                float(i) + 1
            except ValueError:
                if i.lower() == 'stop':
                    print(f'stop-word has been entered!\nYour list: {self.ans}')
                    return
                print(InvData('I can append nums only!'))
            else:
                if int(float(i)) == float(i):
                    self.ans.append(int(float(i)))
                else:
                    self.ans.append(float(i))
        return SuperDuper()


a = SuperDuper()


