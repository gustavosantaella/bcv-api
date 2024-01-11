from fastapi import APIRouter
from src.remote.BcvService import BcvService
from src.helpers.fn import static_response_error
from src.remote.DolarTodayService import DolarTodayService

router = APIRouter(
    prefix="/currency"
)


@router.get("")
def get(tasa: str = 'bcv'):
    try:
        data, error1 = BcvService.values()
        data_dolartoday, error2 = DolarTodayService.check_price_of_dolar()
        if error1 or error2:
            return static_response_error()
        
        return {
            "status":200,
            "data": {
                "bcv": data,
                "dolarToday": {
                    "usd": data_dolartoday
                }
            }
        } 
    except Exception as e:
        print(e)
        return static_response_error(error=e)
    
