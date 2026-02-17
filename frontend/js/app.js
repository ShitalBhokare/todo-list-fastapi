const BASE_URL = "http://127.0.0.1:8000/todos";

let todosData = [];
let editId = null;

document.addEventListener("DOMContentLoaded", loadTodos);

async function loadTodos() {
  try {
    const res = await fetch(BASE_URL);
    todosData = await res.json();
    renderTodos(todosData);
    updateProgress();
  } catch (err) {
    console.error("Error loading todos:", err);
  }
}

function renderTodos(todos) {
  const list = document.getElementById("todoList");
  list.innerHTML = "";

  todos.forEach((todo) => {
    const div = document.createElement("div");
    div.className = "todo-item";
    if (todo.completed) div.classList.add("completed");

    div.innerHTML = `
      <div class="left">
        <input type="checkbox" ${todo.completed ? "checked" : ""} 
        onchange="toggleTodo(${todo.id}, this.checked)">
        <div>
          <h3>${todo.title}</h3>
          <p>${todo.description || ""}</p>
        </div>
      </div>

      <div class="actions">
        <button class="edit-btn" onclick="openModal(${todo.id})">✏</button>
        <button class="delete-btn" onclick="deleteTodo(${todo.id})">🗑</button>
      </div>
    `;

    list.appendChild(div);
  });
}

async function addTodo() {
  const title = document.getElementById("taskTitle").value.trim();
  const description = document.getElementById("taskDesc").value.trim();
  if (!title) return alert("Title required");

  await fetch(BASE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description }),
  });

  document.getElementById("taskTitle").value = "";
  document.getElementById("taskDesc").value = "";
  loadTodos();
}

async function toggleTodo(id, completed) {
  const todo = todosData.find((t) => t.id === id);

  await fetch(`${BASE_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: todo.title,
      description: todo.description,
      completed,
    }),
  });

  loadTodos();
}

async function deleteTodo(id) {
  if (!confirm("Delete this task?")) return;

  await fetch(`${BASE_URL}/${id}`, { method: "DELETE" });
  loadTodos();
}

function openModal(id) {
  const todo = todosData.find((t) => t.id === id);
  editId = id;

  document.getElementById("editTitle").value = todo.title;
  document.getElementById("editDesc").value = todo.description || "";
  document.getElementById("editModal").classList.add("active");
}

function closeModal() {
  document.getElementById("editModal").classList.remove("active");
  editId = null;
}

async function updateTodo() {
  const title = document.getElementById("editTitle").value.trim();
  const description = document.getElementById("editDesc").value.trim();
  if (!title) return alert("Title required");

  const todo = todosData.find((t) => t.id === editId);

  await fetch(`${BASE_URL}/${editId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title,
      description,
      completed: todo.completed,
    }),
  });

  closeModal();
  loadTodos();
}

function searchTodos() {
  const q = document.getElementById("searchInput").value.toLowerCase();
  renderTodos(
    todosData.filter(
      (t) =>
        t.title.toLowerCase().includes(q) ||
        (t.description || "").toLowerCase().includes(q),
    ),
  );
}

function filterTodos(type) {
  if (type === "all") renderTodos(todosData);
  if (type === "completed") renderTodos(todosData.filter((t) => t.completed));
  if (type === "pending") renderTodos(todosData.filter((t) => !t.completed));
}

function updateProgress() {
  const total = todosData.length;
  const completed = todosData.filter((t) => t.completed).length;
  const percent = total ? (completed / total) * 100 : 0;

  document.getElementById("progressFill").style.width = percent + "%";
  document.getElementById("progressText").innerText =
    `${completed} / ${total} Completed`;
}