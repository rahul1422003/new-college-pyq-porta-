# Deployment Guide

## 1. Firebase Firestore setup

Set these environment variables before enabling Firebase sync:

- `FIREBASE_ENABLED=true`
- `FIREBASE_PROJECT_ID=<your-firebase-project-id>`
- `FIREBASE_SERVICE_ACCOUNT_JSON=<full service account json in one line>`

Collections used by the app:

- `userLogins`
- `feedback`
- `placementQuestions`
- `placementResults`

## 2. Database setup

Set:

- `DB_URL`
- `DB_USERNAME`
- `DB_PASSWORD`

## 3. Admin credentials

Set:

- `ADMIN_EMAIL`
- `ADMIN_PASSWORD`

## 4. Render deployment

This project includes `render.yaml`.

Recommended Render env vars:

- `DB_URL`
- `DB_USERNAME`
- `DB_PASSWORD`
- `ADMIN_EMAIL`
- `ADMIN_PASSWORD`
- `FIREBASE_ENABLED`
- `FIREBASE_PROJECT_ID`
- `FIREBASE_SERVICE_ACCOUNT_JSON`

## 5. Local run

```bash
mvn spring-boot:run
```
