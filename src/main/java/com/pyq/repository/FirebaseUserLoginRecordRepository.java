package com.pyq.repository;

import com.google.cloud.firestore.DocumentSnapshot;
import com.pyq.model.UserLoginRecord;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class FirebaseUserLoginRecordRepository extends FirestoreRepositorySupport<UserLoginRecord> implements UserLoginRecordRepository {

    private static final String COLLECTION = "userLogins";

    @Override
    public long count() {
        return count(COLLECTION);
    }

    @Override
    public UserLoginRecord save(UserLoginRecord record) {
        if (record.getId() == 0) {
            record.setId(nextId(COLLECTION, UserLoginRecord::getId));
        }
        memory.put(record.getId(), record);
        firebaseSyncService.syncLoginRecord(record);
        return record;
    }

    @Override
    public List<UserLoginRecord> findAll(Sort sort) {
        return sorted(findAll(COLLECTION, this::fromDocument), UserLoginRecord::getLoginTime, true);
    }

    private UserLoginRecord fromDocument(DocumentSnapshot document) {
        UserLoginRecord record = new UserLoginRecord();
        record.setId(documentId(document));
        record.setName(string(document, "name"));
        record.setEnrollment(string(document, "enrollment"));
        record.setSemester(string(document, "semester"));
        record.setLoginTime(dateTime(document, "loginTime"));
        return record;
    }
}
