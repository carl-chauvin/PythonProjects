#Generacion de reportes automaticamente

import schedule
import time

def GenerateReportAuto():
    print("Report Generation In Process...")

    generate_weekly_report("Excel/salesdaily.csv")

    schedule.every().sunday().at("08:00").do(GenerateReportAuto)

    print("Waiting for the time to Generate the report")

    while True:
        schedule.run_pending()
        time.sleep(2)
