import json
import requests

global_base_url = "http://localhost:3000/todos"
requests_list = [
    {
        "method": "POST",
        "name": "Create Todo",
        "url": global_base_url,
        "headers": {"Content-Type": "application/json"},
        "body": '{"title": "New Todo", "completed": false}'
    },
    {
        "method": "GET",
        "name": "Get Todos",
        "url": global_base_url,
        "headers": {"Content-Type": "application/json"},
        "body": ""
    },
    {
        "method": "PUT",
        "name": "Update Todo",
        "url": global_base_url + "/{todo_id}",  # Replace {todo_id} with the actual ID of the todo to update
        "headers": {"Content-Type": "application/json"},
        "body": '{"title": "Updated Todo", "completed": true}'
    },
    {
        "method": "DELETE",
        "name": "Delete Todo",
        "url": global_base_url + "/{todo_id}",  # Replace {todo_id} with the actual ID of the todo to delete
        "headers": {"Content-Type": "application/json"},
        "body": ""
    }
]

def create_todo_app_collection(collection_name = "TodoAppCollection", base_url = global_base_url):
    """
    Create a Postman collection for testing CRUD operations on a Todo application.

    Returns:
    - str: JSON representation of the Postman collection.
    """    

    # requests_list = [
    #     {
    #         "method": "POST",
    #         "name": "Create Todo",
    #         "url": base_url,
    #         "headers": {"Content-Type": "application/json"},
    #         "body": '{"title": "New Todo", "completed": false}'
    #     },
    #     {
    #         "method": "GET",
    #         "name": "Get Todos",
    #         "url": base_url,
    #         "headers": {"Content-Type": "application/json"},
    #         "body": ""
    #     },
    #     # You can add/update more requests for update (PUT), delete (DELETE), etc.
    # ]

    collection = {
        "info": {
            "name": collection_name,
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": []
    }

    for req in requests_list:
        request_item = {
            "name": req['name'],
            "request": {
                "method": req['method'],
                "header": req['headers'],
                "url": req['url'],
                "body": {
                    "mode": "raw",
                    "raw": req['body']
                }
            }
        }
        collection['item'].append(request_item)

    return json.dumps(collection, indent=2)

def test_create_todo_app_collection():
    collection_json = create_todo_app_collection()

    # You can save the collection JSON to a file or use it with Newman CLI.
    # For example, save to a file:
    with open("todo_app_collection.json", "w") as file:
        file.write(collection_json)
