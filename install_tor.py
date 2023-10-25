"""This script installs Tor on the Raspberry Pi."""

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

# Define a function to install Tor
def install_tor():
  """Install the Tor package."""
  run_command(["sudo", "apt", "update"])
  run_command(["sudo", "apt", "install", "-y", "tor"])

# Execute the function
def main():
  install_tor()

if __name__ == '__main__':
  main()
