# Git Basics

- For this task, I created a Python script using the `requests` library.  
- Then, I created a new branch to add a new "feature" to the file, following these steps:  
- I also created a `.gitignore` file to include files that should not be pushed to the remote repository.

## 1. Creating the Feature Branch

```bash
git checkout -b feature-project-title
````

## 2. After Making Changes, Add and Commit

```bash
git add .
git commit -m "..."
```

## 3. Switch Back to the Main Branch

```bash
git checkout main
```

## 4. Merge the Feature Branch

```bash
git merge feature-project-title
```

## 5. Push the Updated Main Branch to GitHub

```bash
git push origin main
```
