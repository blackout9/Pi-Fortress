"""This script installs StrongSwan on the Raspberry Pi."""

# Imports the subprocess module
import subprocess

# Define a function to run shell commands
def run_command(command: str) -> str:
  """Run a shell command and return the output as a string."""
  try:
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True
    )
    return result.stdout.decode("utf-8")
  except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")
    return e.stderr.decode("utf-8")

# Define a function to install StrongSwan
def install_strongswan():
  """Install StrongSwan and related packages."""
  run_command("sudo apt update")
  run_command("sudo apt install -y strongswan strongswan-pki")

# Execute the function
def main():
  install_strongswan()

if __name__ == '__main__':
  main()
