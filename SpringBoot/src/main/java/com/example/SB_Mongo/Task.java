package com.example.SB_Mongo;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

/**
 * Represents a task with a title, description, and completion status.
 * This class is used to model tasks in a collection named "tasks" in a database.
 * It includes methods to get and set the task's ID, title, description, and completion status.
 * 
 * Example usage:
 * Task task = new Task();
 * task.setTitle("Buy groceries");
 * task.setDescription("Milk, eggs, and bread");
 * task.setCompleted(false);
 * 
 * @Document(collection = "tasks")
 */
public class Task {
    @Id
    private String id;
    private String title;
    private String description;
    private boolean completed;

    // Getters and Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public boolean isCompleted() { return completed; }
    public void setCompleted(boolean completed) { this.completed = completed; }
}
