"""
module for describing the routines
with conditions and changes between them
"""
from random import random


# ROUTINE includes 7 conditions, 3 of them being randomly caused;

class ROUTINE:
    "class describing the routine"
    def __init__(self):
        # initializing states
        self.sleep = self.SLEEP()
        self.sleep.send(None)

        self.plan_the_day = self.PLAN_THE_DAY()
        self.plan_the_day.send(None)

        self.hurry = self.HURRY()
        self.hurry.send(None)

        self.travel = self.TRAVEL()
        self.travel.send(None)

        self.do_the_tasks = self.DO_THE_TASKS()
        self.do_the_tasks.send(None)

        self.correct_errors = self.CORRECT_ERRORS()
        self.correct_errors.send(None)

        self.eat = self.EAT()
        self.eat.send(None)

        # setting current state of the system
        self.current_state = self.sleep

        # stopped flag to denote that iteration is stopped due to bad
        # input against which transition was not defined.
        self.stopped = False

    def send(self, char):
        """The function sends the curretn input to the current state
        It captures the StopIteration exception and marks the stopped flag.
        """
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True

    def go_on(self):
        """The function checks for `stopped` flag which
        sees that due to bad input the iteration had to be stopped.
        """
        if self.stopped:
            return False
        return True

    def SLEEP(self):
        "sleep condition"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if char == 'wake up':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.plan_the_day
                print('---You wake up---')
                print('Now you are planning your day')
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break

    def PLAN_THE_DAY(self):
        "condition of planning the day"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            # the random events are possible as well
            if random() < 0.9:
                self.current_state = self.hurry
                print("You definitely didn't expect it, but you are late for classes!")
                print("..You have no time to waste")
                print('Now you are in a hurry')
            elif random() < 0.3:
                print('You did not expect to discover all classes were cancelled!')
                print('..You decided to use this day to travel')
                print('Now you are travelling')
                self.current_state = self.travel
            elif char == 'start working':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.do_the_tasks
                print('--You start working on the tasks--')
                print('Now you are working on the tasks')
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break

    def HURRY(self):
        "being in a hurry condition"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if char == 'hurry':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.do_the_tasks
                print("--You started working on the tasks on time--")
                print('Now you are working on the tasks')
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break

    def TRAVEL(self):
        "travelling condition"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if char == 'time to sleep':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.sleep
                print("--You decided it's time to end your journey and sleep--")
                print("Now you are sleeping")
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break

    def DO_THE_TASKS(self):
        "condition of doing the tasks"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if random() < 0.3:
                print("You suddenly do the error in the calculations!")
                print("..You have to correct it")
                print("Now you are correcting the error in the task")
                self.current_state = self.correct_errors
            elif char == 'time to eat':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.eat
                print("--You decided it's time to eat--")
                print("Now you are eating")
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break

    def CORRECT_ERRORS(self):
        "condition of correcting errors"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if char == 'errors corrected':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.do_the_tasks
                print("--You correct all the errors--")
                print("Now you continue to do your tasks")
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break

    def EAT(self):
        "condition of eating"
        while True:
            # Wait till the input is received.
            # once received store the input in `char`
            char = yield

            # depending on what we received as the input
            # change the current state of the fsm
            if char == 'time to sleep':
                # on receiving `b` the state moves to `q2`
                self.current_state = self.sleep
                print("--You decide it's time to sleep--")
                print("Now you are sleeping")
            else:
                # on receiving any other input, break the loop
                # so that next time when someone sends any input to
                # the coroutine it raises StopIteration
                break



def start_routine():
    "starts the routine"
    print('You are sleeping')
    evaluator = ROUTINE()
    while True:
        answ = input('waiting for further changes...    ')
        print()
        evaluator.send(answ)
        if not evaluator.go_on():
            print('Wrong input. The routine had to be stopped.')
            break

start_routine()
