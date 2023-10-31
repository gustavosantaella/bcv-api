from fastapi import APIRouter
from src.remote.BcvService import BcvService
from src.helpers.fn import static_response_error
router = APIRouter(
    prefix="/currency"
)


@router.get("")
def get(tasa: str = 'bcv'):
    data, error = BcvService.values()
    if error:
        return static_response_error()
    
    return {
        "status":200,
        "data": data
    } 