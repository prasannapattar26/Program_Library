from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def String(request):
    return render(request, 'String.html')


def s1(request):
    return render(request, 's1.html')


def tests1(request):
    sentence = request.GET['scr']
    ls = sentence.split()
    sen_new = ""
    ls1 = ls[::-1]
    for word in ls1:
        sen_new = sen_new + " " + word
    sen_new = sen_new.strip()
    res = "The reversed sentence is : " + sen_new
    print(sentence)
    return render(request, 's1.html', {'result': res})


def s2(request):
    return render(request, 's2.html')


def tests2(request):
    sen = request.GET['scr']
    counter = 0
    for i in sen:
        counter += 1
    res = ("Total chars. : " + str(counter))
    return render(request, 's2.html', {'result': res})


def s3(request):
    return render(request, 's3.html')


def tests3(request):
    sen = request.GET['scr']
    counter = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for char in sen:
        for vow in vowel:
            if char.lower() == vow:
                counter += 1
    res = (counter)
    return render(request, 's3.html', {'result': res})


def s4(request):
    return render(request, 's4.html')


def tests4(request):
    sen = request.GET['scr']
    sen1 = ""
    counter = 0
    for i in sen:
        sen1 += i
        counter += 1
    res = "The number of characters copied are : " + str(counter)
    return render(request, 's4.html', {'result': res})


def Simple(request):
    return render(request, 'Simple.html')


def n1(request):
    return render(request, 'n1.html')


def testn1(request):
    n = request.GET['scr']
    d = int(n)
    if d % 365 == 0:
        years = int(d / 365)
        days = 0
    else:
        years = int(d / 365)
        days = d % 365
    if days % 30 == 0:
        months = days / 30
        days1 = 0
    else:
        months = int(days / 30)
        days1 = days % 30
    res = ("The value converted to {:} years , {:} months , {:} days".format(years, months, days1))
    return render(request, 'n1.html', {'result': res})


def n2(request):
    return render(request, 'n2.html')


def testn2(request):
    ID = request.GET['scr1']
    hrs = request.GET['scr2']
    amt = request.GET['scr3']
    salary = int(hrs) * int(amt)
    res = ("Salary of Employee with id {:} is Rs{:}".format(ID, salary))
    return render(request, 'n2.html', {'result': res})


def n3(request):
    return render(request, 'n3.html')


def testn3(request):
    nu1 = int(request.GET['scr1'])
    nu2 = int(request.GET['scr2'])
    nu3 = int(request.GET['scr3'])
    if nu1 > nu2 and nu1 > nu3:
        res = "number1 is the greatest if the three"
    elif nu2 > nu1 and nu2 > nu3:
        res = "number2 is the greatest of the three"
    else:
        res = "number3 is the greatest of the three"
    return render(request, 'n3.html', {'result': res})


def n4(request):
    return render(request, 'n4.html')


def testn4(request):
    # Taking 2000,500,100,20,10 Notes

    amt1 = request.GET['scr']
    res1000 = 0
    res500 = 0
    res100 = 0
    res20 = 0
    res10 = 0
    amt = int(amt1)
    if amt % 2000 == 0:
        two1000 = int(amt / 2000)
        res1000 = "Rs 2000 notes :" + str(two1000)

    else:
        two1000 = int(amt / 2000)
        amt = amt % 2000
        res1000 = "Rs 2000 notes :" + str(two1000)

        if amt % 500 == 0:
            five100 = int(amt / 500)
            res500 = "Rs 500 notes :" + str(five100)

        else:
            five100 = int(amt / 500)
            amt = amt % 500
            res500 = "Rs 500 notes :" + str(five100)
            if amt % 100 == 0:
                one100 = int(amt / 100)
                res100 = "Rs 100 notes :" + str(one100)
            else:
                one100 = int(amt / 100)
                amt = amt % 100
                res100 = "Rs 100 notes :" + str(one100)
                if amt % 20 == 0:
                    two10 = int(amt / 20)
                    res20 = "Rs 20 notes :" + str(two10)
                else:
                    two10 = int(amt / 20)
                    amt = amt % 20
                    res20 = "Rs 20 notes :" + str(two10)
                    if amt % 10 == 0:
                        one10 = int(amt / 10)
                        res10 = "Rs 10 notes :" + str(one10)
                    else:
                        one10 = int(amt / 10)
                        amt = amt % 10
                        res10 = "Rs 10 notes :" + str(one10)
    return render(request, 'n4.html',
                  {'result2000': res1000, 'result500': res500, 'result100': res100, 'result20': res20,
                   'result10': res10})


def n5(request):
    return render(request, 'n5.html')


def testn5(request):
    sec1 = request.GET['scr']
    sec = int(sec1)
    if sec % 3600 == 0:
        hours = int(sec / 3600)
        sec = 0
    else:
        hours = int(sec / 3600)
        sec = sec % 3600
    if sec % 60 == 0:
        minutes = sec / 60
        sec = 0
    else:
        minutes = int(sec / 60)
        sec = sec % 60
    res = ("The value converted to {:} hours , {:} minutes , {:} seconds".format(hours, minutes, sec))
    return render(request, 'n5.html', {'result': res})


def n6(request):
    return render(request, 'n6.html')


def testn6(request):
    num_list = list()
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    for i in [n1, n2, n3, n4, n5]:
        num_list.append(int(i))
    sum1 = 0
    for n in num_list:
        if not int(n) % 2 == 0:
            sum1 = sum1 + int(n)
        else:
            continue
    res = ("Sum of Odd values is :" + str(sum1))
    return render(request, 'n6.html', {'result': res})


def n7(request):
    return render(request, 'n7.html')


def testn7(request):
    n1 = request.GET['scr']
    n = int(n1)
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    res = ("The month resembling the value entered is :", months[n - 1])
    return render(request, 'n7.html', {'result': res})


def n8(request):
    return render(request, 'n8.html')


def testn8(request):
    n = []
    for i in range(2):
        n.append(input(request.GET['scr']))
    if not int(n[1]) == 0:
        res = ("The result of division is :", (float(n[0]) / float(n[1])))
    else:
        res = "Division not possible"
    return render(request, 'n8.html', {'result': res})


def n9(request):
    return render(request, 'n9.html')


def testn9(request):
    cm1 = request.GET['scr']
    cm = float(cm1)
    inches = cm / 2.54
    res = ("The length in inches is :", inches)
    return render(request, 'n9.html', {'result': res})


def n10(request):
    return render(request, 'n10.html')


def testn10(request):
    n1 = int(request.GET['scr1'])
    n2 = int(request.GET['scr2'])
    n3 = 0
    n3 = n1
    n1 = n2
    n2 = n3
    res = ("The swapped values :" + n1 + "," + n2)
    return render(request, 'n10.html', {'result': res})


def n11(request):
    return render(request, 'n11.html')


def testn11(request):
    n1 = int(request.GET['scr1'])
    n2 = int(request.GET['scr2'])
    n1 = n1 + n2
    n2 = n1 - n2
    n1 = n1 - n2
    res = ("The number of n1 : {:} & n2 : {:} after swapping ".format(n1, n2))
    return render(request, 'n11.html', {'result': res})


def Array(request):
    return render(request, 'Array.html')


def a1(request):
    return render(request, 'a1.html')


def testa1(request):
    num_list = []
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    n6 = request.GET['scr6']
    n7 = request.GET['scr7']
    for i in [n1, n2, n3, n4, n5, n6, n7]:
        num_list.append(int(i))
    res1 = ("The value at element number : 1 is {:}".format(n1))
    res2 = ("The value at element number : 2 is {:}".format(n2))
    res3 = ("The value at element number : 3 is {:}".format(n3))
    res4 = ("The value at element number : 4 is {:}".format(n4))
    res5 = ("The value at element number : 5 is {:}".format(n5))
    res6 = ("The value at element number : 6 is {:}".format(n6))
    res7 = ("The value at element number : 7 is {:}".format(n7))
    return render(request, 'a1.html',
                  {'result1': res1, 'result2': res2, 'result3': res3, 'result4': res4, 'result5': res5, 'result6': res6,
                   'result7': res7})


def a2(request):
    return render(request, 'a2.html')


def testa2(request):
    num_list = []
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    for i in [n1, n2, n3, n4, n5]:
        num_list.append(int(i))
    num_list1 = []
    for n in num_list:
        counter = 0
        n = int(n)
        for i in range(1, n + 1):
            if n % i == 0:
                counter += 1
        if counter == 2:
            num_list1.append(n)
    res = "List of prime numbers in the entered array is :" + str(num_list1)
    return render(request, 'a2.html', {'result': res})


def a3(request):
    return render(request, 'a3.html')


def testa3(request):
    num_list = []
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    for i in [n1, n2, n3, n4, n5]:
        num_list.append(int(i))
    res = []
    i = 1
    for n in num_list:
        n = int(n)
        if n < 5:
            res.append("The element at position {:} whose value is {:} less than 5.".format(i, n))
        i += 1
    return render(request, 'a3.html', {'result': res})


def a4(request):
    return render(request, 'a4.html')


def testa4(request):
    num_list = []
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    n6 = request.GET['scr6']
    for i in [n1, n2, n3, n4, n5, n6]:
        num_list.append(i)
    reverse = []
    res1 = "Original list is :" + str(num_list)
    num_list.reverse()
    for n in num_list:
        reverse.append(n)
    res2 = "Reversed list is :" + str(reverse)
    return render(request, 'a4.html', {'result1': res1, 'result2': res2})


def a5(request):
    return render(request, 'a5.html')


def testa5(request):
    num_list = []
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    n6 = request.GET['scr6']
    for i in [n1, n2, n3, n4, n5, n6]:
        num_list.append(i)
    small_num = None
    small_pos = None
    i = 1
    for n in num_list:
        n = int(n)
        if small_num is None:
            small_num = n
            small_pos = i
        elif n < small_num:
            small_num = n
            small_pos = i
        i += 1
    res = ("The smallest number is {:} at the position : {:}.".format(small_num, small_pos))
    return render(request, 'a5.html', {'result': res})


def Loop(request):
    return render(request, 'Loop.html')


def l1(request):
    return render(request, 'l1.html')


def testl1(request):
    num = []
    n1 = request.GET['scr1']
    n2 = request.GET['scr2']
    n3 = request.GET['scr3']
    n4 = request.GET['scr4']
    n5 = request.GET['scr5']
    n6 = request.GET['scr6']
    n7 = request.GET['scr7']
    n8 = request.GET['scr8']
    n9 = request.GET['scr9']
    n10 = request.GET['scr10']
    for i in [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]:
        num.append(i)
    sum = 0
    for n in num:
        sum += int(n)
    avg = sum / 10
    res = ("Sum : {:}  &  Average : {:.1f}".format(sum, avg))
    return render(request, 'l1.html', {'result': res})


def l2(request):
    return render(request, 'l2.html')


def testl2(request):
    n1 = int(request.GET['scr1'])
    product = 1
    for i in range(3):
        product = product * n1
    res = "The product is : " + str(product)
    return render(request, 'l2.html', {'result': res})


def l3(request):
    return render(request, 'l3.html')


def testl3(request):
    n = int(request.GET['scr'])
    num_list = []
    for i in range(10):
        product = 1
        product = n * (i + 1)
        num_list.append("{:>2} * {:<2} = {:>1}  ".format(n, (i + 1), product))

    return render(request, 'l3.html', {'result': num_list})


def l4(request):
    return render(request, 'l4.html')


def testl4(request):
    n = int(request.GET['scr'])
    sum = 0
    for i in range(1, (n)):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        res = "Perfect number"
    else:
        res = "Not a Perfect number"
    return render(request, 'l4.html', {'result': res})


def l5(request):
    return render(request, 'l5.html')


def testl5(request):
    n1 = int(request.GET['scr1'])
    n2 = int(request.GET['scr2'])
    num_list = []
    for n in range(n1, n2 + 1):
        sum = 0

        for i in range(1, n):
            if n % i == 0:
                sum = sum + i
        if sum == n:
            num_list.append(" {:} is a perfect number.".format(sum))
        else:
            num_list.append(" {:} is not a perfect number.".format(n))

    return render(request, 'l5.html', {'result': num_list})


def l6(request):
    return render(request, 'l6.html')


def testl6(request):
    n1 = int(request.GET['scr1'])
    n2 = int(request.GET['scr2'])
    sum = 0
    for n in range(n1, n2 + 1):
        if not n % 17 == 0:
            sum += n
    res = ("The sum of numbers in the range not divisible by 17 is {:} .".format(sum))
    return render(request, 'l6.html', {'result': res})


def l7(request):
    return render(request, 'l7.html')


def testl7(request):
    num = int(request.GET['scr'])
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        res = "The entered number is prime."
    else:
        res = "The entered number is not prime."
    return render(request, 'l7.html', {'result': res})


def l8(request):
    return render(request, 'l8.html')


def testl8(request):
    num = int(request.GET['scr'])
    product = 1
    for i in range(1, num + 1):
        product *= i
    res = ("The factorial of the entered number is : " + str(product))
    return render(request, 'l8.html', {'result': res})


def l9(request):
    return render(request, 'l9.html')


def testl9(request):
    n1 = int(request.GET['scr1'])
    n2 = int(request.GET['scr2'])
    num_list = []
    for num in range(n1, n2 + 1):
        counter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                counter += 1

        if counter == 2:
            num_list.append("The number {:} is prime.  ".format(num))
        else:
            num_list.append("The number {:} is not prime.  ".format(num))
    return render(request, 'l9.html', {'result': num_list})


def l10(request):
    return render(request, 'l10.html')


def testl10(request):
    num = int(request.GET['scr'])
    num1 = num
    sum = 0
    while num1 > 0:
        m = num1 % 10
        sum = sum + m ** 3
        num1 = num1 // 10
    if sum == num:
        res = "The entered number is armstrong."
    else:
        res = "The entered number is not armstrong."
    return render(request, 'l10.html', {'result': res})


def l11(request):
    return render(request, 'l11.html')


def testl11(request):
    num_list = []
    for n in range(1, 1001):
        sum1 = 0
        m = n
        while m > 0:
            a = m % 10
            sum1 += a ** 3
            m = m // 10
        if sum1 == n:
            num_list.append("The number {:} is armstrong.  ".format(n))
        else:
            num_list.append("The number {:} is not armstrong.  ".format(n))
    return render(request, 'l11.html', {'result': num_list})


def l12(request):
    return render(request, 'l12.html')


def testl12(request):
    num_list = []
    n1 = int(request.GET['scr1'])
    n2 = int(request.GET['scr2'])
    for n in range(n1, n2 + 1):
        if n < 7:
            continue
        if not n % 7 == 0:
            if n % 7 == 2 or n % 7 == 3:
                m = n % 7
                num_list.append("{:} being divided by 7 leaves remainder {:}.  ".format(n, m))
    return render(request, 'l12.html', {'result': num_list})


def l13(request):
    return render(request, 'l13.html')


def testl13(request):
    n = int(request.GET['scr'])
    num_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            num_list.append("{:} is a divisor for the entered number.  ".format(i))
    return render(request, 'l13.html', {'result': num_list})


def l14(request):
    return render(request, 'l14.html')


def testl14(request):
    n = int(request.GET['scr'])
    sum1 = 0
    m = n
    while m > 0:
        a = m % 10
        sum1 = sum1 * 10 + a
        m = m // 10
    res = ("The reverse of the entered number is : " + str(sum1))
    return render(request, 'l14.html', {'result': res})





