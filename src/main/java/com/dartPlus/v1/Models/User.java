package com.dartPlus.v1.Models;

import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.List;

@Entity
@Data
@Table(name = "dartPlusUser")
@NoArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "id", nullable = false)
    private Long id;

    private String firstName;
    private String lastName;

//    @Column(unique=true)
//    private String email;

    @ManyToOne
//    @JoinColumn(name="board_id", nullable = false)
    private Board board;

    @ManyToMany(mappedBy = "users")
    private List<Game> posts;

    public User(String firstName, String lastName, Board board) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.board = board;
    }

    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}