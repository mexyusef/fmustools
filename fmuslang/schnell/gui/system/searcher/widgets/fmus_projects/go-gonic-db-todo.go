package database

import (
	"database/sql"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

func InitDB() *sql.DB {
	db, err := sql.Open("sqlite3", "./todo.db")
	if err != nil {
		log.Fatal(err)
	}

	createTable(db)

	return db
}

func createTable(db *sql.DB) {
	query := `
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            completed INTEGER
        );
    `
	_, err := db.Exec(query)
	if err != nil {
		log.Fatal(err)
	}
}
