#!/usr/bin/env python3

import os, cmd

class ShellEnabled(cmd.Cmd):
    
    def do_shell(self, line) -> None:
        command = os.popen(line)
        print(command.read())
    
    def do_echo(self, line):
        print(line)

    def do_EOF(self, line) -> bool:
        return True
    
    def postloop(self) -> None:
        print("Bye :(")

if __name__ == "__main__":
    ShellEnabled().cmdloop()