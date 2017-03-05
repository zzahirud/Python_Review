#-------------------------------------------------------------------------------
# Name:        webscraping_icddesc
# Purpose:      This script can be used to get icd description for a given number of dx by making web calls to the CMS.
#
# Author:      zubair.zahiruddin
#
# Created:     26/08/2015
# Copyright:   (c) zubair.zahiruddin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#importing libraries

import csv
import requests, bs4
import pyodbc


# connecting to db and executing query
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=TESTABC;DATABASE=TESTDB;UID=user;PWD=password')
cursor = cnxn.cursor()
cursor.execute("select icdcode, icddesc from missing_icd where ICDDESC = 'no desc'")
result_set = cursor.fetchall()

#putting results in a list

list_missing_icd = []
for row in result_set:
    #print row.user_id, row.user_name
    list_missing_icd.append(row.icdcode)

#global function

def is_ascii(s):
    t = ''
    for al in s:
        if ord(al) < 128:
            t += al
    return t


icd_descriptions = []

#dictionary to hold icd codes, icd descriptions after making the web request to the CMS website.
dictionary = {}

def get_desc(list_missing_icd):

    for element in list_missing_icd:
        element = element[0:3] + '.' + element[3:]
        print element
        # making a web call to get description
        s = 'https://www.cms.gov/medicare-coverage-database/staticpages/icd-9-code-lookup.aspx?KeyWord='
        s = s + element
        res = requests.get(s)
        res.raise_for_status()
        noStarchSoup = bs4.BeautifulSoup(res.text)
        elems = noStarchSoup.select('.gridviewRow td')
        if elems == []:
            print ('could not find description')
            dictionary[element] = 'no desc'
            cursor.execute("insert into missing_icd (ICDCODE, ICDDESC) values (?, ?)", element, dictionary[element])
            cnxn.commit()
        else:

            elems = noStarchSoup.select('.gridviewRow td')
            st = (elems[1].getText())
            st = is_ascii(st)
            #print st;
            icd_descriptions.append (st)
            dictionary[element] = (st)
            cursor.execute("insert into Missing_ICD (ICDCODE, ICDDESC) values (?, ?)", element, dictionary[element])
            cnxn.commit()

    return dictionary;

#Running the function to test the get_desc function
print get_desc(list);


with open('C:/Users/XYZ/ABC/klm.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(dictionary.items())
