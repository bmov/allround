import os
from dotenv import dotenv_values

default_env = None

if os.getenv('ALLROUND_MODE') == 'prod':
    default_env = dotenv_values(".env.dev")
else:
    default_env = dotenv_values(".env.prod")

env = {
    **dotenv_values(".env.server"),
    **default_env,
    **dotenv_values(".env"),
    **os.environ,
}
