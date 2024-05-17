#!/usr/bin/env python3

import cmd

class HelloWorld(cmd.Cmd):
    def do_greet(self, person) -> str:
        if person: 
            print("Hello, ", person)
        else: 
            print("Hello :)")

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
