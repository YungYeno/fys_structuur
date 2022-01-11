# Author - Yeno Reus, IC106E
import os
from colorama import init, Fore

# initialize colours
init()

GREEN = Fore.GREEN
RED = Fore.RED
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE


# Super cool intro :)
def intro():
    print(f"""{MAGENTA}
███████ ██    ██ ███████     ██ ███    ██ ███████ ████████  █████  ██      ██      ███████ ██████  
██       ██  ██  ██          ██ ████   ██ ██         ██    ██   ██ ██      ██      ██      ██   ██ 
█████     ████   ███████     ██ ██ ██  ██ ███████    ██    ███████ ██      ██      █████   ██████  
██         ██         ██     ██ ██  ██ ██      ██    ██    ██   ██ ██      ██      ██      ██   ██ 
██         ██    ███████     ██ ██   ████ ███████    ██    ██   ██ ███████ ███████ ███████ ██   ██ """)


# Install the needed requirements
def requirements():
    print(f"{GREEN}\nInstalling the project requirements...{WHITE}")
    command = "sudo apt install git python3-flask python3-flask-login python3-flask-sqlalchemy"
    try:
        result = os.system(command)
        print(result)
    except OSError as error:
        print(f"{RED}\nSomething went wrong with installing requirements! : {WHITE}{error}")


# Clone the github project
def get_project():
    print(f"{GREEN}\nDownloading project files...{WHITE}")
    command = "git clone https://github.com/YungYeno/fys_structuur.git"
    try:
        result = os.system(command)
        print(result)
    except OSError as error:
        print(f"{RED}\nSomething went wrong with getting project files : {error}")


# Move files to proper location
def moving_files():
    path = "fys_structuur/"
    print(f"{GREEN}\nAdding files to the wsgi folder...{WHITE}")
    commands = ["sudo mv project /var/www/fys/wsgi",
                "sudo mkdir /var/www/fys/corendon",
                f"sudo mv {path}*.html {path}db.sqlite {path}requirements.txt {path}templates /var/www/fys/wsgi/",
                f"sudo mv {path}corendon.conf /etc/apache2/sites-available"]
    try:
        for command in commands:
            result = os.system(command)
            print(result)
    except OSError as error:
        print(f"{RED}\nSomething went wrong trying to move the files: {error}")


# Set the right permissions
def permissions():
    print(f"{GREEN}\nSetting permissions...{WHITE}")
    commands = ["sudo chmod 777 -R /var/www/fys/wsgi",
                "sudo chmod 777 /etc/apache2/sites-available/corendon.conf"]
    try:
        for command in commands:
            result = os.system(command)
            print(result)
    except OSError as error:
        print(f"{RED}\nSomething went wrong setting the permissions : {error}")


# Let user know that script is completed.
def outro():
    print(f"{GREEN}\nScript completed! {WHITE}Restart apache2 with {MAGENTA}'systemctl restart apache2'")


if __name__ == '__main__':
    intro()
    # requirements()
    # get_project()
    # moving_files()
    # permissions()
    # outro()
