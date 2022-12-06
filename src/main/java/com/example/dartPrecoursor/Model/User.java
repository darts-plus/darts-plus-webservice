package com.example.dartPrecoursor.Model;

import lombok.Data;

import javax.persistence.*;

@Entity
@Data
@Table(name = "dartPlusUser")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private long id;
    private String firstName;
    private String lastName;

    @Column(unique=true)
    private String email;

    @ManyToOne
    private Board usedBoard;
}