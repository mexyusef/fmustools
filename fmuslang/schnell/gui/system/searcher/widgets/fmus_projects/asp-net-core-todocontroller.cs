using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using TodoApp.Models;

namespace TodoApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TodoController : ControllerBase
    {
        private static List<Todo> todos = new List<Todo>();

        [HttpGet]
        public IEnumerable<Todo> Get()
        {
            return todos;
        }

        [HttpPost]
        public IActionResult Create(Todo todo)
        {
            todo.Id = todos.Count + 1;
            todo.CreatedAt = DateTime.Now;
            todos.Add(todo);
            return Ok(todo);
        }
    }
}
