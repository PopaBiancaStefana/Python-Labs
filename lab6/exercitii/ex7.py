import re




def verify_cnp(cnp):
    return re.match(r"[1256][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])[0-9]{4}", cnp) is not None

def main():
    print(verify_cnp("6991214270876"))


if __name__ == '__main__':
    main()
