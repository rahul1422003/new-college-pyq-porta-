package com.pyq.util;

import java.time.LocalDateTime;
import java.time.ZoneId;

public final class AppClock {

    public static final ZoneId INDIA_ZONE = ZoneId.of("Asia/Kolkata");

    private AppClock() {
    }

    public static LocalDateTime now() {
        return LocalDateTime.now(INDIA_ZONE);
    }
}
