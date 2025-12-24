from fastapi.responses import JSONResponse


def success(data=None, hint="调用成功"):
    return JSONResponse(content={
        "successful": "true",
        "resultValue": data,
        "resultHint": hint,
        "resultCode": 200
    })


def fail(result_code=500, hint="调用失败"):
    return JSONResponse(content={
        "successful": "false",
        "resultValue": None,
        "resultHint": hint,
        "resultCode": result_code
    })
