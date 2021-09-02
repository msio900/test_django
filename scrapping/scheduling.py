import schedule
import time

def job01():
    print('job01() working ....')
    # return

def job02(param01, param02):
    print('job02() working ....', param01, param02)



schedule.every(1).minutes.do(job01)
schedule.every().day.at('14:30').do(job01)

schedule.every(1).minutes.do(job02, 'p01', 'p02')


while True:
    schedule.run_pending()
    time.sleep(1)