#!/usr/bin/env python3

import cmd

class HelloWorld(cmd.Cmd):

    def do_greet(self, args) -> str:
        print("Hello :)")

    def do_EOF(self, args) -> bool:
        return True
    
if __name__ == "__main__":
    HelloWorld().cmdloop()
