from resources.users import createUser, getUser, updateUser, deleteUser

endPoints_list = [
    {"resource": createUser, "url": '/add'},
    {"resource": getUser, "url": '/all'},
    {"resource": updateUser, "url": '/update/<int:user_id>'},
    {"resource": deleteUser, "url": '/delete/<int:user_id>'},
]