package controllers

import javax.inject._
import play.api.mvc._
import play.api.libs.json._
import play.api.data._
import play.api.data.Forms._
import models.Todo

@Singleton
class TodoController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {

  // Define a form mapping for creating a new todo
  val todoForm: Form[Todo] = Form {
    mapping(
      "id" -> ignored(0L),
      "title" -> nonEmptyText,
      "description" -> nonEmptyText
    )(Todo.apply)(Todo.unapply)
  }

  // Action to render the list of todos
  def index: Action[AnyContent] = Action { implicit request =>
    val todos = Todo.getAll() // Replace with your logic to fetch todos from a database or any other source
    Ok(Json.toJson(todos))
  }

  // Action to create a new todo
  def createTodo: Action[AnyContent] = Action { implicit request =>
    todoForm.bindFromRequest.fold(
      formWithErrors => {
        BadRequest("Invalid todo data")
      },
      todoData => {
        val savedTodo = Todo.save(todoData) // Replace with your logic to save the todo
        Created(Json.toJson(savedTodo))
      }
    )
  }

  // Action to delete a todo
  def deleteTodo(id: Long): Action[AnyContent] = Action { implicit request =>
    val deleted = Todo.delete(id) // Replace with your logic to delete the todo
    if (deleted) Ok("Todo deleted") else NotFound("Todo not found")
  }
}
