"""
This script configures Tor by appending settings to the torrc file and starts the Tor service. It also sets up firewall rules specific to Tor.
"""

import subprocess


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


def configure_tor():
  """
  Configure Tor by appending settings to the torrc file.
  Adjust based on specific needs and refer to the official Tor documentation.
  """
  tor_config = """
  # Sample Tor configuration
  SocksPort 9050
  Log notice file /var/log/tor/notices.log
  ControlPort 9051
  """
  with open("/etc/tor/torrc", "a") as f:
    f.write(tor_config)


def start_tor():
  """Start the Tor service and enable it to start on boot."""
  run_command("sudo systemctl start tor")
  run_command("sudo systemctl enable tor")


def setup_firewall_rules():
  """Set up firewall rules specific to Tor."""
  run_command("sudo ufw allow 9050/tcp")  # Tor SOCKS proxy


# Execute the functions
def main():
  configure_tor()
  start_tor()
  setup_firewall_rules()

if __name__ == '__main__':
  main()
