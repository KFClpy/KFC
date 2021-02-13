def state_confirm(string):
    s=string.split("|")
    return s[0]
def state_blind(string):
    s=string.split("|")
    return s[1]
if __name__=="__main__":
    string=input()
    print(state_confirm(string))
    print(state_blind(string))
