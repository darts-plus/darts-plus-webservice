package com.dartPlus.v1.Models;

import lombok.Data;

import javax.persistence.*;

@Entity
@Data
@Table(name = "player")
public class Player {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "id", nullable = false)
    private Long id;

    @ManyToOne
    private Game game;

}