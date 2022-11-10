# CS61Lab4

we have submitted the following files:

- getDatabase.py
- Team23Lab2.ini
- frontEnd.py
- testfile.in
- testfile.out
- A folder *commands*, containing the following files:
    - comment.py
    - delete.py
    - post.py
    - show.py

## Build/Run 
To run the front-end application, ensure that you are in a python environment for databases (as described in Lab 0) and that the environment has been activated. From there, run `python3 frontEnd.py` to load the application, and enter inputs via the command line as prompted.

## Testing: 
To test run the front end application and pipe in a list of requests commands from a `testfile.in` and output the results to an `.out` file. The provided testfile creates a blog engine with two blogs. The first blog is the 'politics' blog and attempts to replicate the example provided on the assignment. The second blog is just a simple blog where a couple different posts and comments are added and edge cases are tested such as no tags or a referenced permalink doesn't exist. Running `python lab4 < testfile1.in 2>&1 grader.testfile1.out` will create the two blogs and output the results to `grader.testfile1.out`. This file should be identical to `testfile.out` whch can be seen with `diff grader.testfile1.out testfile1.out` 

## Notes
- Schema Design: We considered embeding our posts and comments but decided agains it so we could more easily seach the documents directly with the permalink. We decided on created three collection, `blogs`, `posts`, and`comments`. Each blog document contains a list of post permalinks contained inside it, each post document contains a list of comment permalinks contained inside it, and each comment document contains a list of replied comments permalinks contained inside it,
- In delete, we assume that only the body of the post/comment is deleted and the post title as well as all comments/replies remain intact; We also assume that anyone may delete a post or comment, even if they are not the author. For posts - timestamp is updated. For comments - we cannot change the permalink (it's permanent!) so we add a new timestamp field
- We standardized post permalinks to reference the post's title. This aligns with the lab specs, does not allow for duplicate posts within a blog to have the same title, and furthermore conflicts with the example test provided in the specs. Ensure during testing, when attempting to comment on or delete a post, that the permalink properly refers to the post's title, rather than its timestamp.

*** TO ASK IN OFFICE HOURS ***:
For delete: 
- when deleting, is only the body replaced with the delete message? do we remove the title? is the original timestamp replaced or is a new field added with the deletion timestamp?
- for a comment, we cannot change the permalink—should we then add a new field with the deletion timestamp?
- do we leave all comments and replies intact, and display them all for show?