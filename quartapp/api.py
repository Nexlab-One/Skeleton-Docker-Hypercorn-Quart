
import asyncio
from quart import Quart, request, jsonify
from quart_schema import QuartSchema, validate_request, validate_response

app = Quart(__name__)
QuartSchema(app)

@app.route('/')
async def home():
    '''Note Route

    This docstring will show up as the description and short-description
    for the openapi docs for this route.
    '''
    return jsonify({"Note": "There exists a localhost:9000/openapi.json that can be helpful here"})

if __name__ == "__main__":
    app.run(host='localhost', 
        port=8080, 
        certfile='cert.pem', 
        keyfile='key.pem')
