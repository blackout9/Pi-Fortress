import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        return e.stderr.decode('utf-8')

def install_tor():
    """Install the Tor package."""
    run_command("sudo apt update")
    run_command("sudo apt install -y tor")

# Execute the function
install_tor()
