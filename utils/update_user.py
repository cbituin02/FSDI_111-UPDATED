import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"

def update_user(user_data, user_id):
    url = "%s/%s/" % (URL, user_id)
    response=requests.put(url, json=user_data)
    if response.status_code == 204:
        print("Successfuly updated user.")
    else:
        print("Something went wrong while trying to update user.")


def get_user(user_id):
    url = "%s/%s/" % (URL, user_id)
    response = requests.get(url)
    if response.status_code == 200:
        print("User: ")
        pprint(response.json())
        return response.json().get("user")[0]
    else:
        print("Something went wrong while trying to retrieve the user.")
        return ""
    

if __name__ == "__main__":
    user_id = input("Type in the users's id: ")
    target_user = get_user(int(user_id))
    first_name = input("Type in a new frist name (or leave blank): ")
    last_name = input("Type ins a new last name (or leave blank) ")
    hobbies = input("Type in new hobbies (or leave blank): ")
    if first_name:
        target_user["first_name"] = first_name
    if last_name:
        target_user["last_name"] = last_name
    if hobbies:
        target_user["hobbies"] = hobbies
    update_user(target_user, user_id)
    option = input("Would you like to see the updated user? [Y/N] ")
    if option == "Y" or option == "y":
        get_user(user_id)