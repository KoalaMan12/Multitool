import os

def check_and_install(package_name, command):
    """Checks if a package is installed. If not, installs it."""
    print(f"Checking for {package_name}...")
    check_command = f"dpkg -l | grep -i {package_name}"
    result = os.system(check_command)

    if result != 0:
        print(f"{package_name} is not installed. Installing...")
        os.system(f"sudo apt-get install -y {command}")
    else:
        print(f"{package_name} is already installed.")

# Clear terminal screen
os.system('clear')

# Print menu
print("""

#     #                                                  
##   ## #    # #      ##### # #####  ####   ####  #      
# # # # #    # #        #   #   #   #    # #    # #      
#  #  # #    # #        #   #   #   #    # #    # #      
#     # #    # #        #   #   #   #    # #    # #      
#     # #    # #        #   #   #   #    # #    # #      
#     #  ####  ######   #   #   #    ####   ####  ######

""")
print("Choose one of the options:")
print("Setoolkit: 1")
print("Metasploit: 2")
print("Wireshark: 3")
print("sqlmap: 4")
print("Bettercap: 5")
print("Credits: 6")

input_choice = input()

if input_choice == '1':
    check_and_install("setoolkit", "setoolkit")
    print("Setoolkit running...")
    os.system("setoolkit")
elif input_choice == '2':
    check_and_install("metasploit-framework", "metasploit-framework")
    print("Metasploit running...")
    os.system("msfconsole")
elif input_choice == '3':
    check_and_install("wireshark", "wireshark")
    print("Wireshark running...")
    os.system("wireshark") 
elif input_choice == '4':
    check_and_install("sqlmap", "sqlmap")
    print("sqlmap running...")
    os.system("sqlmap --wizard")
elif input_choice == '5':
    check_and_install("bettercap", "bettercap")
    print("bettercap running...")
    os.system("bettercap")
elif input_choice == '6':
    os.system("cat credits.txt")
else:
    print("Invalid option selected. Please choose a valid number.")
