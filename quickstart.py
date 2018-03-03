from instapy import InstaPy
import schedule
import time

insta_username = 'alda.bot'
insta_password = ''  # fill in password


def job():
    try:
        session = InstaPy(username=insta_username,
                          password=insta_password,
                          headless_browser=False,
                          multi_logs=True,
                          nogui=True)
        session.login()

        # settings
        # session.set_upper_follower_count(limit=2500)
        # session.set_do_comment(True, percentage=10)
        # session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
        # session.set_dont_include(['friend1', 'friend2', 'friend3'])
        # session.set_dont_like(['pizza', 'girl'])

        # actions
        session.like_by_tags(['barcelona', 'madrid'], amount=100)
        session.end()
    except:
        import traceback
        print(traceback.format_exc())


schedule.every().day.at("10:00").do(job)
schedule.every().day.at("11:30").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("14:30").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("17:30").do(job)
schedule.every().day.at("19:00").do(job)
schedule.every().day.at("20:30").do(job)
schedule.every().day.at("22:00").do(job)
schedule.every().day.at("23:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
