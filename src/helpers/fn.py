def static_response_error() -> dict[str, str]:
    return {
            "status": 400,
            "message": "An error ocurred. You can report this with a issue in https://github.com/gustavosantaella/bcv-api/issues"
        }