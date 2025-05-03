package com.example.SB_Mongo;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * TaskController is a REST controller for managing tasks.
 * It provides endpoints to retrieve, create, update, and delete tasks.
 * 
 * Core functionalities:
 * - getAllTasks(): Retrieves all tasks from the repository.
 * - createTask(Task task): Creates a new task and saves it to the repository.
 * - updateTask(String id, Task task): Updates an existing task in the repository.
 * - deleteTask(String id): Deletes a task from the repository.
 * 
 * Usage:
 * - To retrieve all tasks, make a GET request to /tasks.
 * - To create a new task, make a POST request to /tasks with the task details in the request body.
 * - To update an existing task, make a PUT request to /tasks/{id} with the updated task details in the request body.
 * - To delete a task, make a DELETE request to /tasks/{id}.
 * 
 * Constructor:
 * - TaskController(TaskRepository taskRepository): Initializes the TaskController with the provided TaskRepository.
 * 
 * Parameters:
 * - TaskRepository taskRepository: The repository used to interact with the task data.
 * 
 * Usage example:
 * 
 * // Create a new task
 * Task newTask = new Task();
 * newTask.setName("New Task");
 * newTask.setDescription("This is a new task");
 * 
 * // Save the new task
 * Task savedTask = taskController.createTask(newTask);
 * 
 * // Update an existing task
 * savedTask.setDescription("Updated description");
 * Task updatedTask = taskController.updateTask(savedTask.getId(), savedTask);
 * 
 * // Delete a task
 * taskController.deleteTask(updatedTask.getId());
 */
@RestController
@RequestMapping("/tasks")
public class TaskController {

    // Inject the TaskRepository
    @Autowired
    private TaskRepository taskRepository;

    // Get all tasks
    @GetMapping
    public List<Task> getAllTasks() {
        return taskRepository.findAll();
    }

    // Create a new task
    @PostMapping
    public Task createTask(@RequestBody Task task) {
        return taskRepository.save(task);
    }

    // Update an existing task
    @PutMapping("/{id}")
    public Task updateTask(@PathVariable String id, @RequestBody Task task) {
        task.setId(id);
        return taskRepository.save(task);
    }

    // Delete a task
    @DeleteMapping("/{id}")
    public void deleteTask(@PathVariable String id) {
        taskRepository.deleteById(id);
    }
}
