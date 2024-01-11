from fastapi import FastAPI
from dotenv import load_dotenv
from src.modules.api.currency.controller import router
import uvicorn

from apscheduler.schedulers.background import BackgroundScheduler
# from remote.DolarTodayService import DolarTodayService
load_dotenv()


app = FastAPI()


app.include_router(router, prefix="/api")



# @app.on_event("startup")
# def startup():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(lambda: MonitorDolarService.check_price_of_dolar(True), 'cron', minute=59)
#     scheduler.start()
#     print("Jobs are working")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)