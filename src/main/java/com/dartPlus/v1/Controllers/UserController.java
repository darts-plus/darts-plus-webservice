package com.dartPlus.v1.Controllers;

import com.dartPlus.v1.Models.Board;
import com.dartPlus.v1.Models.User;
import com.dartPlus.v1.Repositories.UserRepository;
import com.dartPlus.v1.Services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping(path = "api/v1/users")
public class UserController {

    @Autowired
    private UserService userService;

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public List<User> getUsers(){
        Board board1 = new Board();
        userService.deleteAllUsers();
        userService.saveUser("Artur", "Zilas", board1);
        userService.saveUser("Anna", "Drabinka", board1);
        return userService.findAllUsers();
    }
}
