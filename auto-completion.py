#!/usr/bin/env python3

import cmd

class HelloWorld(cmd.Cmd):
    
    PERSONS = ["Abdisa", "Abdiza", "Iza"]

    def do_greet(self, person) -> str:
        if person: 
            print("Hello, ", person)
        else: 
            print("Hello :)")

    def complete_greet(self, text, line, beginx, endidx) -> list:
        if text:
            completions = [person for person in self.PERSONS if person.startswith(text)]
        else:
            completions = self.PERSONS
        return completions

    def do_EOF(self, args) -> bool:
        return True
    
    def help_greet(self) -> bool | None:
        print("\n".join(["Greet [person]", "Greet the named person"]))

    def preloop(self) -> None:
        print("Welcome :)")
    
    def postloop(self) -> None:
        print("Bye :(")
            
if __name__ == "__main__":
    HelloWorld().cmdloop()
