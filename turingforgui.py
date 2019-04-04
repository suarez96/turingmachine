class TM:
    tape = list()

    def __init__(self, f, t):
        # read file
        self.file = open(f, "r")
        lines = self.file.readlines()
        # make states
        self.currentState = int(lines[5])
        self.acceptState = int(lines[7])
        self.accept = False
        self.reject = False
        # make transitions
        self.transitions = list()
        self.transitionList = lines[3].split(';')
        self.transitionList.remove('\n')
        for i in range(len(self.transitionList)):
            self.transitionList[i] = self.transitionList[i][1:-1]
            self.transitionList[i] = self.transitionList[i].split(',')

        for i in self.transitionList:
            (ins, outs) = ((int(i[0]), i[1]), (int(i[2]), i[3], i[4]))
            self.transitions.append((ins, outs))
        # initial tape head position and tape input
        self.head = 0
        self.tapeString = t
        for i in self.tapeString:
            self.tape.append(i)
        print("initial state: {n}, initial input {i}, head in: {h}".format(n = self.currentState, i = self.tape[self.head], h = self.head))

    def goto(self, nextState, write, move):
        self.currentState = nextState
        if self.acceptState == self.currentState:
            print("accepted, final configuration:")
            print(self.tape)
            self.accept = True
            return
        if write != '':
            self.tape[self.head] = write
            print("writing {w} over position: {h}".format(w = write, h = self.head))

        self.head = self.head + 1 if move == 'R' else self.head - 1
        print(self.tape)
        print("new state: {n}, new input '{i}', head moved {m} to : {h}".format(n = self.currentState, i = self.tape[self.head], m = move, h = self.head))

    def runTM(self):
        if self.accept is False and self.reject is False:
            found = False
            for tr in self.transitions:
                if (self.currentState, str(self.tape[self.head])) == tr[0]:
                    self.goto(tr[1][0], tr[1][1], tr[1][2])
                    found = True
                    break
            if not found:
                self.reject = True
                print("rejected")

