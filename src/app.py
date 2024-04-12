from flask_openapi3 import OpenAPI
from flask_openapi3 import Info
from src.route1 import rota1
from src.route3 import rota3

info = Info(title="API Demo", version="0.0.1")

# jwt = {
#     "type": "http",
#     "scheme": "bearer",
#     "bearerFormat": "JWT"
# }

# security_schemes = {"jwt": jwt}

app = OpenAPI(
    __name__,
    info=info,
    # security_schemes=security_schemes,
)
app.register_api(rota1.api)
app.register_api(rota3.api)

print(app.url_map)
