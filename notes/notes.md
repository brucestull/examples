# Notes:

## `git stash`
* `git stash`
* `git stash show`
* `git stash pop`

## Code Examples:

### Goal: Stash changes to `notes.md` and add those changes to branch `main`.

1. `git status`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git status
            On branch 4-document-how-choices-works-in-django
            Your branch is up to date with 'origin/4-document-how-choices-works-in-django'.

            Changes not staged for commit:
            (use "git add <file>..." to update what will be committed)
            (use "git restore <file>..." to discard changes in working directory)
                    modified:   notes.md

            Untracked files:
            (use "git add <file>..." to include in what will be committed)
                ...

            no changes added to commit (use "git add" and/or "git commit -a")
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git branch`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git branch
            * 4-document-how-choices-works-in-django
              main
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git stash`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git stash
            Saved working directory and index state WIP on 4-document-how-choices-works-in-django: 3d2ff3c Django 'choices' documentation in progress. Not sure if I'll pursue this further. It's a learning process.
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git status`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git status
            On branch 4-document-how-choices-works-in-django
            Your branch is up to date with 'origin/4-document-how-choices-works-in-django'.

            Untracked files:
            (use "git add <file>..." to include in what will be committed)
            ...

            nothing added to commit but untracked files present (use "git add" to track)
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git checkout main`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git checkout main
            Switched to branch 'main'
            Your branch is up to date with 'origin/main'.
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git branch`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git branch
              4-document-how-choices-works-in-django
            * main
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git stash show`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git stash show
             django/django_field_choices/notes/notes.md | 7 ++++---
             1 file changed, 4 insertions(+), 3 deletions(-)
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git stash pop`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git stash pop
            CONFLICT (modify/delete): django/django_field_choices/notes/notes.md deleted in Updated upstream and modified in Stashed changes. Version Stashed changes of django/django_field_choices/notes/notes.md left in tree.
            On branch main
            Your branch is up to date with 'origin/main'.

            Unmerged paths:
              (use "git restore --staged <file>..." to unstage)
              (use "git add/rm <file>..." as appropriate to mark resolution)
                    deleted by us:   notes.md

            Untracked files:
              (use "git add <file>..." to include in what will be committed)
                    ...

            no changes added to commit (use "git add" and/or "git commit -a")
            The stash entry is kept in case you need it again.
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git rm .\notes.md`
    * Sample output:
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git rm .\notes.md
            rm 'django/django_field_choices/notes/notes.md'
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git status`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git status
            On branch main
            Your branch is up to date with 'origin/main'.

            Untracked files:
            (use "git add <file>..." to include in what will be committed)
                    ../../README.md
                    ../../django_function_and_class_based_detail_views/
                    ../../django_template_basic/
                    ../../../markdown/
                    ../../../notes/

            nothing added to commit but untracked files present (use "git add" to track)
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git checkout 4-document-how-choices-works-in-django`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git checkout 4-document-how-choices-works-in-django
            Switched to branch '4-document-how-choices-works-in-django'
            Your branch is up to date with 'origin/4-document-how-choices-works-in-django'.
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. `git status`
    * Sample output:

            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes> git status
            On branch 4-document-how-choices-works-in-django
            Your branch is up to date with 'origin/4-document-how-choices-works-in-django'.

            Untracked files:
            (use "git add <file>..." to include in what will be committed)
                    ../../README.md
                    ../../django_function_and_class_based_detail_views/
                    ../../django_template_basic/
                    ../../../markdown/
                    ../../../notes/

            nothing added to commit but untracked files present (use "git add" to track)
            PS C:\Users\Bruce\Programming\examples\django\django_field_choices\notes>

1. **SUMMARY:** Should not have used `git rm .\notes.md` above. Need to understand what the output above that step meant.
    * Need to understand the following:
    
            Unmerged paths:
                (use "git restore --staged <file>..." to unstage)
                (use "git add/rm <file>..." as appropriate to mark resolution)
                    deleted by us:   notes.md