package handlers

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/your-username/todo-app/database"
	"github.com/your-username/todo-app/models"
)

func IndexHandler(c *gin.Context) {
	c.HTML(http.StatusOK, "index.html", nil)
}

func TodoListHandler(c *gin.Context) {
	todos := database.GetTodos()
	c.HTML(http.StatusOK, "todos.html", gin.H{"todos": todos})
}

func CreateTodoHandler(c *gin.Context) {
	title := c.PostForm("title")

	todo := models.Todo{
		Title:     title,
		Completed: false,
	}
	database.CreateTodo(&todo)

	c.Redirect(http.StatusSeeOther, "/todos")
}

func DeleteTodoHandler(c *gin.Context) {
	id, _ := strconv.Atoi(c.Param("id"))

	database.DeleteTodoByID(id)

	c.Redirect(http.StatusSeeOther, "/todos")
}
