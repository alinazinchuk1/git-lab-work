#!/usr/bin/env python3

def greet(name: str) -> str:
    return f"Привіт, {name}!"

def farewell(name: str) -> str:
    return f"До побачення, {name}!"

if __name__ == "__main__":
    print(greet("Студент"))
    print(farewell("Студент"))
