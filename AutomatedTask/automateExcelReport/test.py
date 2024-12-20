#Generacion de reportes automaticamente
import schedule
import time
import os

def GenerateReportAuto():
    print("Report Generation In Process...")

automate_excelReport("supermarket_sales.xlsx")

print(f"Report generated at: {os.getcwd()}")

schedule.every().tuesday().at("10:12").do(GenerateReportAuto)

print("Waiting for the time to Generate the report")

while True:
    schedule.run_pending()
    time.sleep(1)
