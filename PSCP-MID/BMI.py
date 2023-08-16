"""DAY1"""
def main():
    """A"""
    name = []
    kg_ = []
    cm_ = []
    name.append(input())
    kg_.append(input())
    cm_.append(input())
    name.append(input())
    kg_.append(input())
    cm_.append(input())
    name.append(input())
    kg_.append(input())
    cm_.append(input())
    name.append(input())
    kg_.append(input())
    cm_.append(input())
    name.append(input())
    kg_.append(input())
    cm_.append(input())
    print(name[0] + "'s  BMI = %.2f" %(float(kg_[0])/((float(cm_[0])/100)**2)))
    print(name[1] + "'s  BMI = %.2f" %(float(kg_[1])/((float(cm_[1])/100)**2)))
    print(name[2] + "'s  BMI = %.2f" %(float(kg_[2])/((float(cm_[2])/100)**2)))
    print(name[3] + "'s  BMI = %.2f" %(float(kg_[3])/((float(cm_[3])/100)**2)))
    print(name[4] + "'s  BMI = %.2f" %(float(kg_[4])/((float(cm_[4])/100)**2)))
main()