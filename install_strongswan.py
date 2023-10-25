"""This script installs StrongSwan on the Rasberry-Pi."""

# Import the subprocess module
import subprocess

# Uses the 'subprocess' import to run commands through the shell
def run_command(command):
    """Run a shell command."""
    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True
        )
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        return e.stderr.decode("utf-8")

# Installs StrongSwan and related packages
def install_strongswan():
    """Install StrongSwan and related packages."""
    run_command("sudo apt update")
    run_command("sudo apt install -y strongswan strongswan-pki")

# Execute the function
install_strongswan()
