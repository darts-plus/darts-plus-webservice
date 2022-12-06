package com.dartPlus.v1.Models;

import lombok.Data;

import javax.persistence.*;

@Entity
@Data
@Table(name = "settings")
public class Settings {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "id", nullable = false)
    private Long id;

    @OneToOne
    private Game game;

}