def success_response(data, message = "Success"):
    return{
        "Status" : "success",
        "message" : message,
        "data" : data
    }