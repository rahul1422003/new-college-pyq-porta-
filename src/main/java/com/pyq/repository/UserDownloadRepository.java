package com.pyq.repository;

import com.pyq.model.UserDownload;

import java.util.List;

public interface UserDownloadRepository {

    UserDownload save(UserDownload download);

    List<UserDownload> findByEnrollmentOrderByDownloadedAtDesc(String enrollment);

    long countByEnrollment(String enrollment);
}
