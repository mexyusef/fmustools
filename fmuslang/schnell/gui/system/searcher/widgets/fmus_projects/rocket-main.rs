#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

use rocket_contrib::json::Json;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct Todo {
    id: u32,
    title: String,
    completed: bool,
}

#[get("/todos")]
fn get_todos() -> Json<Vec<Todo>> {
    let todos = vec![
        Todo {
            id: 1,
            title: String::from("Finish the Rust project"),
            completed: false,
        },
        Todo {
            id: 2,
            title: String::from("Submit the Rust project"),
            completed: false,
        },
    ];
    Json(todos)
}

fn main() {
    rocket::ignite().mount("/", routes![get_todos]).launch();
}
