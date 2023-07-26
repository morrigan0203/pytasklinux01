import subprocess
import string


def __check_cmd1(cmd, txt):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    out = result.stdout
    if result.returncode == 0 and txt in out:
        return True
    else:
        return False


def __check_cmd2(cmd, txt):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    out = result.stdout
    for c in string.punctuation:
        out = out.replace(c, ' ')
    out = out.replace('\n', '')
    lst = out.split()
    if result.returncode == 0 and txt in lst:
        return True
    else:
        return False


def check_cmd(cmd, txt, advanced=False):
    if advanced:
        return __check_cmd2(cmd, txt)
    else:
        return __check_cmd1(cmd, txt)


if __name__ == "__main__":
    print(check_cmd("cat /etc/os-release", "VERSION"))
    print(check_cmd("cat /etc/os-release", "Jammy", True))
