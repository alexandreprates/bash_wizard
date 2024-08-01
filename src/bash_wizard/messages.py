from bashcolor import colorize, LIGHT_PURPLE, BOLD, UNDERLINE

help = f"Welcome to {colorize('🧙 Bash Wizard', LIGHT_PURPLE)} 🪄\nbash_wizard is an AI-powered wizard that creates bash commands to perform the action you need!\n\nUsage: bash_wizard <command_request>\nArguments:\n\t<command_request>: description of what the command should do.\n\nExample:\n\tbash_wizard remove all __pycache__ dir include subdirs\n\tbash_wizard add a .gitkeep file in all empty subdirs\n"
missing_ollama = "Error connecting to Ollama, check if it is installed correctly and running!"
missing_model = "Downloading Llama3 model! This may take a while, I recommend going for a coffee "
bye = "🧙 Okay bye!"

def thinking(description:str) -> str:
    return f"{colorize('🧙 Bash Wizard', LIGHT_PURPLE)} is solving 🔮 {colorize(description, effects=[UNDERLINE])} 🔮 {colorize('')}"

def output(bash_command:str=None, command_explanation:str=None) -> str:
    return f"{colorize('Bash Wizard', LIGHT_PURPLE, effects=[])} suggests the following command:\n\n🪄 {colorize(bash_command, effects=[BOLD])}{colorize('')}\n\n🧙 Explanation:\n{command_explanation}\n\nDo you want to execute 🪄 {colorize(bash_command, effects=[BOLD])}{colorize('')} (y/[n])? "