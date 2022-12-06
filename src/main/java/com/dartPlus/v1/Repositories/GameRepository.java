package com.dartPlus.v1.Repositories;

import com.dartPlus.v1.Models.Board;
import com.dartPlus.v1.Models.Game;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface GameRepository extends JpaRepository<Game, Long> {

}
