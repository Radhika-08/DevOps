# Git Branching and Merging

Git branching allows developers to work on features independently without affecting the main codebase.

----

## git branch

Lists all available branches.

Syntax:

```bash
git branch
```

Example:

```bash
* main
```

----

## Creating a New Branch

Syntax:

```bash
git checkout -b feature-login
```

Explanation:

Creates a new branch and switches to it immediately.

----

## Switching Branches

Syntax:

```bash
git checkout main
```

Explanation:

Moves from the current branch to another branch.

----

## Making Changes in a Branch

Example:

```bash
echo "Feature Code" > feature.txt
git add .
git commit -m "Added feature"
```

----

## Merging Branches

Syntax:

```bash
git merge feature-login
```

Explanation:

Combines changes from the feature branch into the current branch.

----

## Deleting a Branch

Syntax:

```bash
git branch -d feature-login
```

Explanation:

Removes a branch after it has been merged.

----

## Advantages of Branching

* Parallel development
* Safe experimentation
* Easier collaboration
* Better code management

----

## Git Workflow

1. Create branch
2. Develop feature
3. Commit changes
4. Merge into main branch
5. Push to GitHub

This workflow is commonly used in professional DevOps and software development projects.