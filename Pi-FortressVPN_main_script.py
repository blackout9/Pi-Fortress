import subprocess

def install_strongswan_package():
    run_command("python3 install_strongswan.py")

def setup_pki():
    run_command("python3 install_strongswan.py")

def configure_strongswan_and_security():
    run_command("python3 strongswan_config.py")

def install_tor_package():
    run_command("python3 install_tor.py")

def configure_tor_and_security():
    run_command("python3 tor_config.py")

def start_all_services():
    run_command("python3 start_services.py")

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        return e.stderr.decode('utf-8')

def install_strongswan_package():
    run_command("python3 install_strongswan.py")

def setup_pki():
    run_command("python3 install_strongswan.py")

def configure_strongswan_and_security():
    run_command("python3 strongswan_config.py")

def install_tor_package():
    run_command("python3 install_tor.py")

def configure_tor_and_security():
    run_command("python3 tor_config.py")

def start_all_services():
    run_command("python3 start_services.py")

#Execution order
install_strongswan_package()         # Call the StrongSwan installation script
setup_pki()                          # Call the PKI setup script
configure_strongswan_and_security()  # Call the StrongSwan configuration script
install_tor_package()                # Call the Tor installation script
configure_tor_and_security()         # Call the Tor configuration script
start_all_services()                 # Call the start services script