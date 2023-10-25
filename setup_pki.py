"""This script sets up the Public Key Infrastructure (PKI) for StrongSwan."""

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

# Define a function to set up the PKI
def setup_pki():
  """Set up the Public Key Infrastructure (PKI) for StrongSwan."""

  # Generate the Certificate Authority (CA)
  run_command("ipsec pki --gen --type rsa --size 4096 --outform pem > ca-key.pem")
  run_command("ipsec pki --self --ca --lifetime 3650 --in ca-key.pem --type rsa --dn 'C=US, O=VPN Server, CN=VPN Server Root CA' --outform pem > ca-cert.pem")

  # Generate the VPN server's certificate
  run_command("ipsec pki --gen --type rsa --size 4096 --outform pem > vpn-server-key.pem")
  run_command("ipsec pki --pub --in vpn-server-key.pem --type rsa | ipsec pki --issue --lifetime 1825 --cacert ca-cert.pem --cakey ca-key.pem --dn 'C=US, O=VPN Server, CN=vpn.server.com' --san vpn.server.com --flag serverAuth --flag ikeIntermediate --outform pem > vpn-server-cert.pem")

  # Move the certificates and keys to the appropriate directories
  run_command("sudo cp vpn-server-cert.pem /etc/ipsec.d/certs/")
  run_command("sudo cp vpn-server-key.pem /etc/ipsec.d/private/")
  run_command("sudo cp ca-cert.pem /etc/ipsec.d/cacerts/")

# Execute the function
def main():
  setup_pki()

if __name__ == '__main__':
  main()
