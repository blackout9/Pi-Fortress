"""This script starts the StrongSwan and Tor services and enables them to start on boot."""

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

# Define a function to start the services
def start_services():
  """Start the StrongSwan and Tor services and enable them to start on boot."""

  # Start and enable StrongSwan
  run_command(["sudo", "systemctl", "start", "strongswan"])
  run_command(["sudo", "systemctl", "enable", "strongswan"])

  # Start and enable Tor
  run_command(["sudo", "systemctl", "start", "tor"])
  run_command(["sudo", "systemctl", "enable", "tor"])

# Execute the function
def main():
  start_services()

if __name__ == '__main__':
  main()
