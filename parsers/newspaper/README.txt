We use Linux's Cron to run the engine automatically.

The strategy for scripting is as follows:

1.fetch
fetch.py runs at 00:00 UTC everyday, which is 08:00 Beijing time.

2. detect deletion
exe_detect_del.py runs at 08:00 and 20:00 UTC everyday.

3. detect comparison
exe_detect_cmp.py runs at 12:00 UTC every Monday, Wednesday and Friday.

4. compare
exe_compare.py runs at 22:00 UTC everyday.

5. clean database
exe_cleanDB.py runs at 20:00 UTC every 28th of the month.
- articles before 1st of the month will be deleted from Newshub/articles
- articles before January or July of the year will be deleted from Newshub/deletions

PS:
1. To check if the scripts run properly, go to /var/log/syslog and search for CRON

2. The commands for crontab is listed in file crontab.txt