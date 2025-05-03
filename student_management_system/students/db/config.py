import os
import dotenv
dotenv.load_dotenv()
from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": os.getenv("DB_HOST", "mysql"),
                "port": int(os.getenv("DB_PORT", "3306")),
                "user": os.getenv("DB_USER", "root"),
                "password": os.getenv("DB_PASSWORD", "your_password"),
                "database": os.getenv("DB_NAME", "student_management"),
            }
        }
    },
    "apps": {
        "models": {
            "models": ["db.models.students", "aerich.models"],
            "default_connection": "default",
        }
    }
}

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()