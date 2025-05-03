// filepath: src/main/java/com/example/SB_Mongo/HelloController.java
package com.example.SB_Mongo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/")
    public String hello() {
        return "Hello, Docker!";
    }
}