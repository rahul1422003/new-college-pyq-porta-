package com.pyq.repository;

import com.pyq.model.UserDownload;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface UserDownloadRepository extends JpaRepository<UserDownload, Integer> {

    List<UserDownload> findByEnrollmentOrderByDownloadedAtDesc(String enrollment);

    long countByEnrollment(String enrollment);
}
