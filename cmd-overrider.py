#!/usr/bin/env python3
import cmd

class Illustrate(cmd.Cmd):
    """ Overriding some of cmd methods """

    def cmdloop(self, intro) -> None:
        print("This custom text", intro)
        return super().cmdloop(intro)
    
    def preloop(self) -> None:
        print("Before Loop")

    def postloop(self) -> None:
        print("After Looop")

    def parseline(self, line: str) -> tuple[str | None, str | None, str]:
        print("parse line")
        print(super().parseline(line))
        return super().parseline(line)
    
    def onecmd(self, line: str) -> bool:
        print("One CMD")
        return super().onecmd(line)
    
    def default(self, line: str) -> None:
        print("testing default value")
        return super().default(line)
    
    def do_EOF(self, line):
        print("Bye :(")
        return True
    
if __name__ == "__main__":
    Illustrate().cmdloop("Illustrating CMD")