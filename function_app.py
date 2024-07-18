import azure.functions as func
import logging
# import JSON
# import pandas
# import pandas as pd

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    html_content = req.get_body().decode('utf-8')

    return func.HttpResponse(f"{html_content_str}")