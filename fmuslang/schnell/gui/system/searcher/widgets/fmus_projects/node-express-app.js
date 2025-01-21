const express = require('express');
const sqlite3 = require('sqlite3');
const app = express();
const port = 3000; // Or any other port number you prefer
const db = new sqlite3.Database('./database.db');

// Get all todos
app.get('/todos', (req, res) => {
    db.all('SELECT * FROM todos', (err, rows) => {
        if (err) {
            console.error(err);
            res.status(500).send('Internal Server Error');
        } else {
            res.json(rows);
        }
    });
});

// Add a new todo
app.post('/todos', (req, res) => {
    const { title, completed } = req.body;
    const createdAt = new Date().toISOString();

    db.run('INSERT INTO todos (title, completed, createdAt) VALUES (?, ?, ?)', [title, completed, createdAt], (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Internal Server Error');
        } else {
            res.status(201).send('Todo created successfully');
        }
    });
});

// Update a todo
app.put('/todos/:id', (req, res) => {
    const { id } = req.params;
    const { title, completed } = req.body;

    db.run('UPDATE todos SET title = ?, completed = ? WHERE id = ?', [title, completed, id], (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Internal Server Error');
        } else {
            res.send('Todo updated successfully');
        }
    });
});

// Delete a todo
app.delete('/todos/:id', (req, res) => {
    const { id } = req.params;

    db.run('DELETE FROM todos WHERE id = ?', [id], (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Internal Server Error');
        } else {
            res.send('Todo deleted successfully');
        }
    });
});
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
