#host = 'data.codeup.com'
#username = 'pagel_2184'
#password = 'KgIWHuDKSurpNScoJxhgGWHVtdFz99O0'

def get_db_url(db):
    user = 'pagel_2184'
    host = 'data.codeup.com'
    password = 'KgIWHuDKSurpNScoJxhgGWHVtdFz99O0'
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return url