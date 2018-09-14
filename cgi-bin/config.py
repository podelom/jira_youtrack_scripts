#!usr/bin/python3

jira_altatec = {'e.barnaev': ['dgpbus', 'rotek', 'rustek'],
                'e.zelenov': ['dgpbus', 'DEPTRANS-RFID', 'DGPRFID', 'WH', 'VIDEOAA', 'KAMI', 'FTS', 'DOC', 'RFIDCS', 'DRFID' ],
                'd.sheviakova': ['ROTEK', 'KAMI', 'QPPROVIDER', 'FTS'],
                'l.vasiliev': ['VVV', 'RUSTEK'],
                'a.konoplev': ['ROTEK', 'QPPROC', 'DRFID', 'DGPRFID'],
                'a.vasiliev': ['CRPT'],
                'a.makushev': ['WH', 'LAS', 'DRFID'],
                's.suhorukov': ['ROTEK'],
                'a.v.vasiliev': ['RUSTEK'],
                'm.orischenko': ['ROTEK', 'ROTEK', 'QPVVV', 'QPPROVIDER', 'QPPROC'],
                'y.chernov': ['SAB', 'ROTEK', 'VVV', 'QPPROC', 'DRFID'],
                'a.sheviakov': ['VIDEOAA', 'SA', 'SAB', 'RUSTEK', 'QPADM', 'KAMI', 'JO', 'FTS', 'DRFID'],
                'z.besaev': ['KAMI', 'FTS', 'DRFID', 'DOC', 'ANTEY']
                }
#DGPBUS, RUSTEK, WH, VIDEOAA, SDXOPASS, SA, ROTEK, QPPROVIDER, QPPROC, MEGA, QPADM, KAMI, FTS, DRFID, DOC
jira_dgp = {'e.barnaev': ['bus', 'ugd', 'ugds', 'sa', 'DGPADM'],
             'e.zelenov': ['bus', 'ugd', 'ugds'],
             'm.orischenko': ['bus', 'ugd', 'ugds'],
             'a.konoplev': ['bus', 'ugd', 'ugds'],
             'e.ostretsov': ['bus', 'ugd', 'ugds'],
             'a.v.vasiliev': ['bus', 'ugd', 'ugds'],
             'a.makushev': ['bus', 'ugd', 'ugds'],
             'a.vanushkin': ['bus', 'ugd', 'ugds'],
             'd.sheviakova': ['bus', 'ugd', 'ugds'],
             'e.ostretsov': ['bus', 'ugd', 'ugds'],
             'v.sapunov': ['bus', 'ugd', 'ugds'],
             'z.besaev': ['bus', 'ugd', 'ugds', 'doc'],
             'y.chernov': ['bus', 'ugd', 'ugds'],
             'e.ostretsov': ['bus', 'ugd', 'ugds'],
             'l.vasiliev': ['bus'],
             'a.sheviakov': ['bus', 'ugd', 'ugds', 'sa', 'DGPADM']
             }
youtrack_tkp = {'e.barnaev': 'TKP',
                'm.orischenko': 'TKP',
                'e.ostretsov': 'TKP',
                'a.v.vasiliev': 'TKP',  
                'y.chernov': 'TKP',
                'a.makushev': 'MOBI',
                'a.vasiliev': 'MOBI',
                'e.rumiantseva': 'TKP'
                }
sign_for_jokes = {
                }
emails = {'e.barnaev': 'e.barnaev@altatec.ru'}
emails = {'e.barnaev': 'e.barnaev@altatec.ru',
           'a.sheviakov': 'a.sheviakov@altatec.ru',
           'm.orischenko': 'm.orischenko@altatec.ru',
           'y.chernov': 'y.chernov@altatec.ru',
           'e.zelenov': 'e.zelenov@altatec.ru',
           'e.ostretsov': 'e.ostretsov@altatec.ru',
           'z.besaev': 'z.besaev@altatec.ru',
           'v.sapunov': 'v.sapunov@altatec.ru',
           'd.sheviakova': 'd.sheviakova@altatec.ru',
           'a.vanushkin': 'a.vanushkin@altatec.ru',
           'a.konoplev': 'a.konoplev@altatec.ru',
           'a.v.vasiliev': 'a.v.vasiliev@altatec.ru',
           'l.vasiliev': 'l.vasiliev@altatec.ru',
           'a.vasiliev': 'a.vasiliev@altatec.ru',
           'e.rumiantseva@altatec.ru': 'e.rumiantseva@altatec.ru'
           'a.makushev': 'a.makushev@altatec.ru'
          }

employee = [{
             'name': 'e.barnaev',
             'sex' : 'm',
             'joke_level' : 1
            },
            {
             'name': 'a.sheviakov',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'm.orischenko',
             'sex' : 'm',
             'joke_level' : 1
            },
            {
             'name': 'e.ostretsov',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'e.zelenov',
             'sex' : 'm',
             'joke_level' : 1
            },
            {
             'name': 'z.besaev',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'v.sapunov',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'd.sheviakova',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'a.vanushkin',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'a.konoplev',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'a.v.vasiliev',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'l.vasiliev',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'a.vasiliev',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'y.chernov',
             'sex' : 'm',
             'joke_level' : 0
            },
            {
             'name': 'e.rumiantseva',
             'sex' : 'w',
             'joke_level' : 0
            },
            {
             'name': 'n.zvereva',
             'sex' : 'w',
             'joke_level' : 0
            }
            {
             'name': 'a.makushev',
             'sex' : 'm',
             'joke_level' : 1
            }
            ]