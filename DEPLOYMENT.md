# Render Deployment Guide

## What is already ready

- `render.yaml` is present in the project root
- app port is already configured as `server.port=${PORT:8080}`
- database and admin credentials are env-based
- Firebase sync is optional and can stay disabled

## Required environment variables

Set these in Render:

- `ADMIN_EMAIL`
- `ADMIN_PASSWORD`
- `FIREBASE_ENABLED`
- `FIREBASE_PROJECT_ID`
- `FIREBASE_SERVICE_ACCOUNT_JSON`

## Firebase

Use:

- `FIREBASE_ENABLED=true`
- `FIREBASE_PROJECT_ID=<your-project-id>`
- `FIREBASE_SERVICE_ACCOUNT_JSON=<full service account json in one line>`

Firestore collections used:

- `users`
- `userLogins`
- `feedback`
- `placementQuestions`
- `placementResults`
- `userDownloads`

## Database

The app now uses Firebase Firestore repositories and does not require MySQL for Render startup.

## Important note about uploads

Render web services use an ephemeral filesystem by default. Files inside `uploads/` are not guaranteed to persist after redeploy or restart.

For production, move uploaded files to one of these:

- Firebase Storage
- AWS S3
- Cloudinary
- another persistent object/file storage

## Step-by-step Render deploy

1. Push this project to GitHub.
2. Open Render dashboard.
3. Click `New +`.
4. Choose `Blueprint`.
5. Connect your GitHub repo.
6. Render will detect `render.yaml`.
7. Review the web service config and continue.
8. Add the required environment variables.
9. Click deploy.
10. Wait for build and start to complete.
11. Open the generated Render URL.
12. Test:
   - `/login`
   - `/admin/login`

## Local run

```bash
mvn spring-boot:run
```
