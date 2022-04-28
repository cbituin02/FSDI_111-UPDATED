from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "v_type": result[3],
            "owner_id": result[4]
        }
        out.append(result_dict)
    return out

def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("color"),
        vehicle_dict.get("license_plate"),
        vehicle_dict.get("v_type"),
        vehicle_dict.get("owner_id")
    )
    statement = """
    INSERT INTO vehicle (
        color, 
        license_plate, 
        v_type, 
        owner_id
        ) VALUES (?, ?, ?, ?)
    """

    cursor= get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()

def scan():
    cursor = get_db().execute("SELECT * FROM vehicle", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM vehicle WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("license_plate"),
        vehicle_data.get("v_type"),
        vehicle_data.get("owner_id"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET color=?,
        license_plate=?,
        v_type=?,
        WHERE
        ownder_id=?,
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()