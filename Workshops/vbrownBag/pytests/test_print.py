#!/usr/bin/python3

def test_print():
    print()
    print("Hello, world")

def test_fstring():
    print()
    name='Kevin'
    print(f'Hello, {name}')

class Stack(list):
    def push(self, x):
        self.append(x)

def test_stack_push():
    _stack = Stack()
    _stack.push('foo')
    assert _stack == ['foo']

def test_stack_pop():
    _stack = Stack()
    _stack.push('foo')
    assert _stack.pop() == 'foo'
    assert len(_stack) == 0

def test_():
    ...
