package main

import (
	"github.com/gin-gonic/gin"
	"github.com/your-username/todo-app/database"
	"github.com/your-username/todo-app/handlers"
)

func main() {
	router := gin.Default()

	db := database.InitDB()
	defer db.Close()

	router.GET("/", handlers.IndexHandler)
	router.GET("/todos", handlers.TodoListHandler)
	router.POST("/todos", handlers.CreateTodoHandler)
	router.DELETE("/todos/:id", handlers.DeleteTodoHandler)

	router.Run(":8080")
}
