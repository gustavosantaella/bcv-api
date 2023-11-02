from fastapi import APIRouter
from src.remote.BcvService import BcvService
from src.helpers.fn import static_response_error
from src.remote.monitor_dolar_service import MonitorDolarService

router = APIRouter(
    prefix="/currency"
)


@router.get("")
def get(tasa: str = 'bcv'):
    try:
        data, error1 = BcvService.values()
        data_paralelo, error2 = MonitorDolarService.check_price_of_dolar()
        if error1 or error2:
            return static_response_error()
        
        return {
            "status":200,
            "data": {
                "bcv": data,
                "paralelo": {
                    "dollar": data_paralelo
                }
            }
        } 
    except Exception as e:
        print(e)
        return static_response_error()
    
