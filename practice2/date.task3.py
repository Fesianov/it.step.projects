from datetime import datetime, timedelta

def old_doc(date):
    doc_date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.now()
    ten_years = today - timedelta(days=10*365.25)
    return doc_date < ten_years

date = input('Enter doc date (example: 2024-12-09): ')
result = old_doc(date)
if result:
    print('Document is older than 10 years.')
else:
    print('Document is younger than 10 years.')