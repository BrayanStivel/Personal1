package com.example.colegio.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.colegio.entity.Materia;

@Repository
public interface MateriaRepository extends JpaRepository<Materia, Long> {

}
