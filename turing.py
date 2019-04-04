class TM:
    # make empty list
    tape = list()

    # constructor function

    def __init__(self, startState, head, inputString, acceptState):
        self.currentState = int(startState)
        self.acceptState = int(acceptState)
        self.accept = False
        self.reject = False
        self.head = head
        self.inputString = inputString
        # for every element in input string, add that element to the charArr list
        for i in self.inputString:
            self.tape.append(i)
        print("initial state: {n}, initial input {i}, head in: {h}".format(n = self.currentState, i = self.tape[self.head], h = self.head))

    # transition functions

    def goto(self, nextState, write, move):
        self.currentState = nextState
        #check if we have gotten to accept state
        if self.acceptState == self.currentState:
            print("accepted, final configuration:")
            print(self.tape)
            self.accept = True
            return
        # write only if transition warrants it#
        if write != '':
            self.tape[self.head] = write
            print("writing {w} over position: {h}".format(w = write, h = self.head))

        # move head position depending on if input is 'L' or 'R'
        self.head = self.head + 1 if move == 'R' else self.head - 1
        print(self.tape)
        print("new state: {n}, new input '{i}', head moved {m} to : {h}".format(n = self.currentState, i = self.tape[self.head], m = move, h = self.head))


# open hard coded file
file = open("2comp.txt", "r")
# read all lines into a list called lines
lines = file.readlines()

# split all of transitions into separate elements
transitionList = lines[3].split(';')
transitionList.remove('\n')

# lines[5] "the sixth line" contains the start state, line[7] contains our accept state
# format for TM is (start state, head initial position, input string, accept state)
tm = TM(int(lines[5]), 0, str(input("Enter the input string: ")+ " "), int(lines[7]))

# for every transition:
for i in range(len(transitionList)):
    # remove all the opening and closing parentheses from all the instructions
    transitionList[i] = transitionList[i][1:-1]
    # split individual transition into 5 elements
    transitionList[i] = transitionList[i].split(',')

# make a 2nd list of transitions to append the actual transitions
transitions = list()

for i in transitionList:
    (ins, outs) = ((int(i[0]), i[1]), (int(i[2]), i[3], i[4]))
    transitions.append((ins, outs))

# iterate through the turing tape, starting at initial state and initial head position
while tm.accept is False and tm.reject is False:
    # input just to pause between transitions, completely optional
    input()
    found = False
    for tr in transitions:
        if (tm.currentState, str(tm.tape[tm.head])) == tr[0]:
            tm.goto(tr[1][0], tr[1][1], tr[1][2])
            found = True
            # also unnecessary unless we want to see one transition at a time
            break
    if not found:
        tm.reject = True
        print("rejected")
