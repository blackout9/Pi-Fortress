# This script installs and configures Strongswan and Tor.

import subprocess

def run_command(command: str) -> str:
  """Executes an external command and returns the output as a string."""
  try:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
    return result.stdout.decode('utf-8')
  except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")
    return e.stderr.decode('utf-8')

# Installs the StrongSwan Package.
def install_strongswan_package():
    run_command("python3 install_strongswan.py")

# Sets up the StrongSwan PKI and Certifcate Authority(CA).
def setup_pki():
    run_command("python3 install_strongswan.py")

# Configures StrongSwan and security.
def configure_strongswan_and_security():
    run_command("python3 strongswan_config.py")

# Installs the Tor package.
def install_tor_package():
    run_command("python3 install_tor.py")

# Configures Tor and security.
def configure_tor_and_security():
    run_command("python3 tor_config.py")

# Starts all of the needed services.
def start_all_services():
    run_command("python3 start_services.py")

#Execution order
def main():
    install_strongswan_package()         # Call the StrongSwan installation script
    setup_pki()                          # Call the PKI setup script
    configure_strongswan_and_security()  # Call the StrongSwan configuration script
    install_tor_package()                # Call the Tor installation script
    configure_tor_and_security()         # Call the Tor configuration script
    start_all_services()                 # Call the start services script

if __name__ == '__main__':
    main()
