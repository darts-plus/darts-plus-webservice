package com.dartPlus.v1.Repositories;

import com.dartPlus.v1.Models.Board;
import com.dartPlus.v1.Models.Player;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PlayerRepository extends JpaRepository<Player, Long> {
}
