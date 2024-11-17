
import bleach
from datetime import datetime, timedelta

# Limpia y sanitiza el input del usuario para evitar XSS.
def sanitize_input(user_input):
    return bleach.clean(user_input, tags=[], attributes=[])

# Verifica si el usuario es mayor de 18 años.
def is_adult(day, month, year):

    try:
        birthdate = datetime(year=int(year), month=int(month), day=int(day))
    except ValueError:
        return False
    
    today = datetime.today()
    age_limit_date = today - timedelta(days=18*365)

    return birthdate <= age_limit_date