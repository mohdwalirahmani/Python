# wap to determine wheather the stud has passed or failed. requires total of 40% and 33%
# in each subject. take input from user

sub1 = int(input("Enter the marks of first sub: "))
sub2 = int(input("Enter the marks of second sub: "))
sub3 = int(input("Enter the marks of third sub: "))

total_percentage = (sub1+sub2+sub3) / 300 * 100
print("you got",round(total_percentage,2),"% marks")        # y round isiliye likha h taake decimal k baad sirf 2 digit tk value print kre

if (total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("Congrats u pass")
else:
    print("Better luck next year, you failed")

    # telling his why he failed

    if (sub1<33):
        print("u failed bcoz u have less marks in sub1,i.e: ",sub1)

    if (sub2<33):
        print("u failed bcoz u have less marks in sub2,i.e: ",sub2)

    if (sub3<33):
        print("u failed bcoz u have less marks in sub3,i.e: ",sub3)

    if(total_percentage<40):
        print("u failed bcoz u have less overall percentage,i.e: ",total_percentage)