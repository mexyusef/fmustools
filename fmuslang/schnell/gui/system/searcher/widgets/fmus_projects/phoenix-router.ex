defmodule TodoAppWeb.Router do
  use TodoAppWeb, :router

  # ...

  scope "/", TodoAppWeb do
    pipe_through :browser

    resources "/todos", TodoController
  end

  # ...
end
