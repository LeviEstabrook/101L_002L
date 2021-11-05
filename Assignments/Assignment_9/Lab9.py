'''
CS 101 Lab
Program 9
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must ask user to input a file name, and loop until a valid one is given.
Program must be able to read and sort Crime Data from a csv file.
Program must ouput the month with the highest crime rate,and the offense that occurs the most.
Program must ask user to input an offense and output a formatted report
of zipcodes and how many times the offense occurs in that zipcode.

ERROR HANDLING:

'''

#ALGORITHM

import csv

def month_from_number(num):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    return months[num-1]

def read_in_file(filename=None):
    if filename == None:
        filename = input('Enter the name of the crime data file ==> ')
    while True:
        try:
            file = open(filename, encoding="utf-8")
            file_csv = csv.reader(file)
            listlist = []
            for line in file_csv:
                listlist.append(line)
            file.close()
            return listlist
        except FileNotFoundError:
            print('Could not find the file specified. {} not found'.format(filename))
            filename = input('Enter the name of the crime data file ==> ')
        except:
            print('Sorry, there was an error. Please try again.')
            filename = input('Enter the name of the crime data file ==> ')

def create_reported_date_dict(listlist):
    d = {}
    for x in range(1,len(listlist)):
        if listlist[x][1] not in d:
            d[listlist[x][1]] = 1
        else:
            d[listlist[x][1]] += 1
    return d

def create_reported_month_dict(listlist):
    m = {}
    for x in range(1,len(listlist)):
        month = int(listlist[x][1][0:2])
        if month not in m:
            m[month] = 1
        else:
            m[month] += 1
    return m

def create_offense_dict(listlist):
    o = {}
    for x in range(1,len(listlist)):
        if listlist[x][7] not in o:
            o[listlist[x][7]] = 1
        else:
            o[listlist[x][7]] += 1
    return o

def create_offense_by_zip(listlist):
    z = {}
    for x in range(1,len(listlist)):
        offense = listlist[x][7]
        zipcode = listlist[x][13]
        if offense not in z:
            z[offense] = {zipcode:1}
        elif zipcode not in z[offense]:
            z[offense][zipcode] = 1
        else:
            z[offense][zipcode] += 1
    return z


if __name__ == "__main__":

    listlist = read_in_file()
    reported_date_dict = create_reported_date_dict(listlist)
    reported_month_dict = create_reported_month_dict(listlist)
    offense_dict = create_offense_dict(listlist)
    offense_by_zip = create_offense_by_zip(listlist)

    #print(reported_date_dict)
    #print(reported_month_dict)
    #print(offense_dict)
    #print(offense_by_zip)

    