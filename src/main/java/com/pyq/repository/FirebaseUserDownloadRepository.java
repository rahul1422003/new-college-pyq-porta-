package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.pyq.model.UserDownload;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public class FirebaseUserDownloadRepository extends FirestoreRepositorySupport<UserDownload> implements UserDownloadRepository {

    private static final String COLLECTION = "userDownloads";

    @Override
    public UserDownload save(UserDownload download) {
        if (download.getId() == 0) {
            download.setId(nextId(COLLECTION, UserDownload::getId));
        }
        if (download.getDownloadedAt() == null) {
            download.setDownloadedAt(LocalDateTime.now());
        }
        memory.put(download.getId(), download);
        firebaseSyncService.syncUserDownload(download);
        return download;
    }

    @Override
    public List<UserDownload> findByEnrollmentOrderByDownloadedAtDesc(String enrollment) {
        return sorted(findAll(COLLECTION, this::fromDocument).stream()
                .filter(download -> enrollment != null && enrollment.equalsIgnoreCase(download.getEnrollment()))
                .toList(), UserDownload::getDownloadedAt, true);
    }

    @Override
    public long countByEnrollment(String enrollment) {
        return findByEnrollmentOrderByDownloadedAtDesc(enrollment).size();
    }

    private UserDownload fromDocument(DocumentSnapshot document) {
        UserDownload download = new UserDownload();
        download.setId(documentId(document));
        download.setName(string(document, "name"));
        download.setEnrollment(string(document, "enrollment"));
        download.setSemester(string(document, "semester"));
        download.setPaperName(string(document, "paperName"));
        download.setPaperPath(string(document, "paperPath"));
        download.setDownloadedAt(dateTime(document, "downloadedAt"));
        return download;
    }
}
