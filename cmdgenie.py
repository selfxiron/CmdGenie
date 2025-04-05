import json
import difflib # for fuzzy matching of user input
import subprocess
import os

def load_commands(filepath="commands.json"):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] 'commands.json not found.'")
        return {}
    
def get_best_match(user_input, commands):
    matches = difflib.get_close_matches(user_input, commands.keys(), n=1, cutoff=0.4)
    return matches[0] if matches else None

def run_command(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"[!] Error running command: {e}")

def main():
    os.system('clear')
    print("Welcome to CmdGenie — your terminal command assistant!\n")
    
    commands = load_commands()
    if not commands:
        return
    
    user_input = input("Ask me what you want to do: ").strip().lower()
    match = get_best_match(user_input, commands)

    if match:
        suggested_cmd = commands[match]
        print(f"\n✨ Suggested Command:\n{suggested_cmd}")
        confirm = input("\nRun this command? (y/n): ").strip().lower()
        if confirm == 'y':
            run_command(suggested_cmd)
        else:
            print("Okay! Not running the command.")
    else:
        print("🤷 Sorry, I couldn't find a matching command.")

if __name__ == "__main__":
    main()