package com.example.SB_Mongo;


// Import the MongoRepository interface from the Spring Data MongoDB library
import org.springframework.data.mongodb.repository.MongoRepository;

// Define a TaskRepository interface that extends the MongoRepository interface
public interface TaskRepository extends MongoRepository<Task, String> {
}