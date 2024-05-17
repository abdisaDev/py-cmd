#!/usr/bin/env python3
import cmd

class Config(cmd.Cmd):
    """ Custom configuration for CMD """

    prompt = ">>> "
    intro = "Welcome :)"

    # documentation header
    doc_header = "Custom Documented commands (help)"
    misc_header = "Custom Miscellaneous header"
    undoc_header = "Custom UnDocumented commands (help)"
    ruler = "*"

    def do_greet(self, person) -> str:
        if person: 
            print("Hello, ", person)
        else: 
            print("Hello :)")

    def do_EOF(self, line) -> bool:
        return True
    
    def postloop(self) -> str:
        print("Bye :(")
    
if __name__ == "__main__":
    Config().cmdloop()
