package com.dartPlus.v1.Services;

import com.dartPlus.v1.Models.Board;
import com.dartPlus.v1.Models.User;
import com.dartPlus.v1.Repositories.BoardRepository;
import com.dartPlus.v1.Repositories.UserRepository;
import org.hibernate.type.ListType;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("usersSvc")
public class UserService {

    UserRepository userRepository;
    BoardRepository boardRepository;

    public UserService(UserRepository userRepository, BoardRepository boardRepository) {
        this.userRepository = userRepository;
        this.boardRepository = boardRepository;
    }

    public List<User> findAllUsers() {
        return userRepository.findAll();
    }

    public User saveUser(String firstName, String lastName, Board board) {
        User user = new User(firstName, lastName);
//        boardRepository.save(board);
        userRepository.save(user);
//        userRepository.deleteById((long)1);
        return user;
    }

    public void deleteAllUsers() {
        userRepository.deleteAll();
    }
}
