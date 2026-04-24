package com.pyq.service;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Service
public class FileStorageService {

    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024;
    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("yyyyMMddHHmmss");

    public String storePdf(MultipartFile file, String subject) throws IOException {
        if (file == null || file.isEmpty()) {
            throw new IllegalArgumentException("Please select a PDF file to upload.");
        }

        String originalFilename = file.getOriginalFilename() == null ? "" : file.getOriginalFilename().toLowerCase();
        if (!originalFilename.endsWith(".pdf")) {
            throw new IllegalArgumentException("Only PDF files are allowed.");
        }

        if (file.getSize() > MAX_FILE_SIZE) {
            throw new IllegalArgumentException("File size must be under 10 MB.");
        }

        String cleanSubject = sanitize(subject);
        if (cleanSubject.isBlank()) {
            cleanSubject = "pyq";
        }

        String fileName = cleanSubject + "_" + LocalDateTime.now().format(FORMATTER) + ".pdf";
        String uploadDir = Paths.get(System.getProperty("user.dir"), "uploads").toString();

        File dir = new File(uploadDir);
        if (!dir.exists() && !dir.mkdirs()) {
            throw new IOException("Unable to create upload directory.");
        }

        File destination = new File(dir, fileName);
        file.transferTo(destination);
        return fileName;
    }

    private String sanitize(String value) {
        if (value == null) return "";
        return value.trim().toLowerCase().replaceAll("[^a-z0-9]+", "_");
    }
}
