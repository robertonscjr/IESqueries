from googlesearch import search
import pandas as pd
import requests
import re
import time
import pickle


def find_emails(html):
    r = re.compile(r"\b[A-Z0-9._%+-]+(@|\(at\)|\[at\])[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)
    emailAddresses =r.findall(html) 
    return emailAddresses

csv = "SUP_IES_2019.CSV"

ies_data = pd.read_csv(csv, sep = "|", encoding = "ISO-8859-1")

sg_ies = ies_data['SG_IES']

ies_emails = {}
for ies in sg_ies:
    query = f'{ies} contato'

    ies_emails[ies] = []

    for res in search(query, tld="com.br", num=1, stop=1, pause=30): 
        print(query)
        html_page = requests.get(res).text
        emails = find_emails(html_page)
        ies_emails[ies].extend(emails)

dbfile = open('emails_ies.pkl', 'wb')
pickle.dump(ies_emails, dbfile)
dbfile.close()
