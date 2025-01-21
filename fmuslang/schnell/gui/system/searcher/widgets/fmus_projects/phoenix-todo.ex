defmodule TodoApp.Todo do
  use Ecto.Schema

  schema "todos" do
    field :title, :string
    field :completed, :boolean, default: false
    timestamps()
  end
end
