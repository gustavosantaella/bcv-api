def static_response_error(**kwargs) -> dict[str, str]:
    return {
            "status": 400,
            "message": "An error ocurred. You can report this with a issue in https://github.com/gustavosantaella/bcv-api/issues",
            "error":str(kwargs['error']) if "error" in kwargs else None
        }