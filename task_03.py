import subprocess
if __name__ == "__main__":
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    out = result.stdout
    if result.returncode == 0:
        lst = out.split("\n")
        if 'VERSION_CODENAME=jammy' in lst and 'VERSION="22.04.2 LTS (Jammy Jellyfish)"' in lst:
            print("SUCCESS")
        else:
            print("FAIL")
