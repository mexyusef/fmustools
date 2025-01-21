#[tauri::command]
fn greet(name: String) -> String {
    format!("Hello, {}!", name)
}

fn main() {
    let app = tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .build(tauri::generate_context!())
        .unwrap();

    app.run(|_| Ok(()));
}
