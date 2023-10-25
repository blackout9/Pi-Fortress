import subprocess

# This code configures StrongSwan by setting up ipsec.conf and ipsec.secrets.
# It also sets up the firewall rules and updates the system.

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        return e.stderr.decode('utf-8')

def configure_strongswan():
    """Configure StrongSwan by setting up ipsec.conf and ipsec.secrets."""

    # Configuration for /etc/ipsec.conf
    ipsec_conf = """
config setup
    charondebug="ike 2, knl 2, cfg 2, net 2, esp 2, dmn 2,  lib 2"

conn %default
    ikelifetime=60m
    keylife=20m
    rekeymargin=3m
    keyingtries=1
    authby=rsasig
    keyexchange=ikev2
    ike=aes256gcm16-sha384-modp3072!
    esp=aes256gcm16-sha384-modp3072!

conn myvpn
    left=%any
    leftcert=vpn-server-cert.pem
    leftsubnet=0.0.0.0/0
    right=vpn.server.com
    rightsubnet=10.10.10.0/24
    auto=start
    """

    with open("/etc/ipsec.conf", "w") as f:
        f.write(ipsec_conf)

    # Configuration for /etc/ipsec.secrets
    ipsec_secrets = ": RSA vpn-server-key.pem"

    with open("/etc/ipsec.secrets", "w") as f:
        f.write(ipsec_secrets)


def set_file_permissions():
    run_command("sudo chmod 600 /etc/ipsec.d/private/vpn-server-key.pem")
    run_command("sudo chmod 600 /etc/ipsec.d/cacerts/ca-key.pem")

def setup_firewall_rules():
    run_command("sudo ufw allow 500/udp")  # IKE
    run_command("sudo ufw allow 4500/udp") # NAT-T
    run_command("sudo ufw allow 9050/tcp") # Tor

def update_system():
    run_command("sudo apt update && sudo apt upgrade -y")

# Execute the functions
configure_strongswan()
set_file_permissions()
setup_firewall_rules()
update_system()
