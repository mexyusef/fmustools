# diesel setup akan hasilkan diesel.toml dan schema.rs

#[derive(Queryable)]
pub struct Post {
    pub id: i32,
    pub title: String,
    pub body: String,
    pub published: bool,
}
