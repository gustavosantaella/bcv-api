from fastapi import FastAPI
from dotenv import load_dotenv
from src.modules.api.currency.controller import router
from apscheduler.schedulers.background import BackgroundScheduler
from src.remote.monitor_dolar_service import MonitorDolarService
load_dotenv()


app = FastAPI()


app.include_router(router, prefix="/api")



@app.on_event("startup")
def startup():
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: MonitorDolarService.check_price_of_dolar(True), 'cron', minute=59)
    scheduler.start()
    print("Jobs are working")