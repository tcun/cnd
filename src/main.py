import cmd
from commands.calculate_cr import calculate_party_cr

class DnDConsole(cmd.Cmd):
    intro = "Welcome to the DnD Command Line Tool! Type help or ? to list commands."
    prompt = "(dnd-cli) "

    def do_calculate(self, arg):
        """Calculate CR based on party size and average level.
           Usage: calculate cr <number_of_players> <average_party_level>
        """
        args = arg.split()
        if not args or args[0] != "cr" or len(args) != 3:
            print("Invalid usage. Expected: calculate cr <number_of_players> <average_party_level>")
            return

        try:
            num_players = int(args[1])
            avg_level = int(args[2])
            cr = calculate_party_cr(num_players, avg_level)
            print(f"Recommended CR Encounters for the party:")
            print(f"  Easy: {cr['Easy']}")
            print(f"  Medium: {cr['Medium']}")
            print(f"  Hard: {cr['Hard']}")
            print(f"  Deadly: {cr['Deadly']}")
        except ValueError:
            print("Please provide valid integers for number_of_players and average_party_level.")

    def do_exit(self, arg):
        """Exit the DnD CLI."""
        return True
    
    def cmdloop(self, intro=None):
        # This will replace the default cmdloop to catch KeyboardInterrupt.
        while True:
            try:
                super(DnDConsole, self).cmdloop(intro=intro)
                self.postloop()
                break
            except KeyboardInterrupt:
                print("^C")
                print("Exiting the DnD CLI.")
                break


if __name__ == "__main__":
    DnDConsole().cmdloop()
