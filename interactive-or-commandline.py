import cmd

class HelloWorld(cmd.Cmd):

    prompt = ''
    use_rawinput = False

    def do_greet(self, args) -> str:
        print("Hello :)")

    def do_EOF(self, args) -> bool:
        return True
    
if __name__ == "__main__":
    import sys
    input = open(sys.argv[1], "rt")
    if len(sys.argv) > 1:
        HelloWorld().onecmd(' '.join(sys.argv[1:]))
    else:
        HelloWorld(stdin=input).cmdloop()
        