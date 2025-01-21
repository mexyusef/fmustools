package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
	_ "github.com/mattn/go-sqlite3"
)

type Todo struct {
	ID     int    `json:"id"`
	Task   string `json:"task"`
	Status string `json:"status"`
}

func main() {
	// Create a new Echo instance
	e := echo.New()

	// Set up the routes
	e.GET("/todos", getTodos)
	e.POST("/todos", createTodo)
	e.PUT("/todos/:id", updateTodo)
	e.DELETE("/todos/:id", deleteTodo)

	// Start the server
	e.Start(":8000")
}

func getTodos(c echo.Context) error {
	// Open the SQLite database file
	db, err := sql.Open("sqlite3", "todos.db")
	if err != nil {
		return err
	}
	defer db.Close()

	// Query all todos from the database
	rows, err := db.Query("SELECT id, task, status FROM todos")
	if err != nil {
		return err
	}
	defer rows.Close()

	// Create a slice to hold the todos
	todos := []Todo{}

	// Iterate over the rows and populate the todos slice
	for rows.Next() {
		var todo Todo
		err := rows.Scan(&todo.ID, &todo.Task, &todo.Status)
		if err != nil {
			return err
		}
		todos = append(todos, todo)
	}

	// Return the todos as JSON
	return c.JSON(http.StatusOK, todos)
}

func createTodo(c echo.Context) error {
	// Parse the request body into a Todo struct
	todo := new(Todo)
	if err := c.Bind(todo); err != nil {
		return err
	}

	// Open the SQLite database file
	db, err := sql.Open("sqlite3", "todos.db")
	if err != nil {
		return err
	}
	defer db.Close()

	// Insert the new todo into the database
	_, err = db.Exec("INSERT INTO todos (task, status) VALUES (?, ?)", todo.Task, todo.Status)
	if err != nil {
		return err
	}

	// Return a success message
	return c.String(http.StatusCreated, "Todo created successfully")
}

func updateTodo(c echo.Context) error {
	// Parse the todo ID from the URL
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return err
	}

	// Parse the request body into a Todo struct
	todo := new(Todo)
	if err := c.Bind(todo); err != nil {
		return err
	}

	// Open the SQLite database file
	db, err := sql.Open("sqlite3", "todos.db")
	if err != nil {
		return err
	}
	defer db.Close()

	// Update the todo in the database
	_, err = db.Exec("UPDATE todos SET task = ?, status = ? WHERE id = ?", todo.Task, todo.Status, id)
	if err != nil {
		return err
	}

	// Return a success message
	return c.String(http.StatusOK, fmt.Sprintf("Todo %d updated successfully", id))
}

func deleteTodo(c echo.Context) error {
	// Parse the todo ID from the URL
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return err
	}

	// Open the SQLite database file
	db, err := sql.Open("sqlite3", "todos.db")
	if err != nil {
		return err
	}
	defer db.Close()

	// Delete the todo from the database
	_, err = db.Exec("DELETE FROM todos WHERE id = ?", id)
	if err != nil {
		return err
	}

	// Return a success message
	return c.String(http.StatusOK, fmt.Sprintf("Todo %d deleted successfully", id))
}
