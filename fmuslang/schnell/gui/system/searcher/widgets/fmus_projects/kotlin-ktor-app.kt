import io.ktor.application.*
import io.ktor.features.ContentNegotiation
import io.ktor.features.StatusPages
import io.ktor.http.HttpStatusCode
import io.ktor.http.content.resources
import io.ktor.http.content.static
import io.ktor.jackson.jackson
import io.ktor.request.receive
import io.ktor.response.respond
import io.ktor.routing.*
import io.ktor.server.engine.embeddedServer
import io.ktor.server.netty.Netty

fun Application.module() {
    install(ContentNegotiation) {
        jackson {}
    }

    install(StatusPages) {
        exception<Throwable> { cause ->
            call.respond(HttpStatusCode.InternalServerError, cause.localizedMessage)
        }
    }

    routing {
        static("/static") {
            resources("static")
        }

        route("/api/todo") {
            get {
                call.respond(/* Get all todos */)
            }

            post {
                val todo = call.receive<Todo>()
                /* Create a new todo */
                call.respond(HttpStatusCode.Created, todo)
            }

            delete("/{id}") {
                val id = call.parameters["id"]
                /* Delete todo with the given id */
                call.respond(HttpStatusCode.NoContent)
            }
        }
    }
}

data class Todo(val id: String, val title: String, val completed: Boolean)

fun main() {
    embeddedServer(Netty, port = 8080, module = Application::module).start(wait = true)
}
