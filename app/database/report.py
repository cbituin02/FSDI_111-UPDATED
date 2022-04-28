from app.database import get_db

def get_all_user_vehicles(user_id):
    statement = """
        SELECT  user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.license_plate,
            vehicle.color,
            vehicle_type.description
        From user
        INNER JOIN vehicle ON user.id = vehicle.owner_id
        INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;
    """
    cursor = get_db()
    cursor.execute(statement, ())
    rsults = cursor.fetchall()
    results = cursor.fetchall()
    cursor.close()
    out = []
    for result in results:
        temp_dict = {
            "last_name": result[0],
            "first_name": result [1],
            "hobbies" : result[2],
            "user_active": result[3],
            "vehicle_license_plate": result[4],
            "vehicle_color": result[5],
            "vehicle_description" : result[6]
        }
        out.append(temp_dict)
    return out
