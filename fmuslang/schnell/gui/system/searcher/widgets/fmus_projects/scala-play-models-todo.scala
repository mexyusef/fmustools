package models

import play.api.libs.json._

case class Todo(id: Long, title: String, description: String)

object Todo {
  var todos: List[Todo] = List.empty

  def getAll(): List[Todo] = todos

  def save(todo: Todo): Todo = {
    val newTodo = todo.copy(id = todos.length + 1)
    todos = newTodo :: todos
    newTodo
  }

  def delete(id: Long): Boolean = {
    val initialSize = todos.length
    todos = todos.filterNot(_.id == id)
    todos.length < initialSize
  }

  implicit val todoFormat: OFormat[Todo] = Json.format[Todo]
}
