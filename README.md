# CS61Lab4

## Build/Run 
To run the front-end application, ensure that you are in a python environment for databases (as described in Lab 0) and that the environment has been activated. From there, run `python3 frontEnd.py` to load the application, and enter inputs via the command line as prompted.

## Testing: 
To test run the front end application and pipe in a list of requests commands from a `testfile.in` and output the results to an `.out` file. The provided testfiles are:

- **politics**
  - *content*: an attempts to replicate the example provided on the assignment
  - *run*: `python frontEnd.py < testFiles/polticsBlogs.in 2>&1 testFiles/grader.polticsBlogs.out`
  - *verify*: `diff testFiles/grader.polticsBlogs.out testFiles/polticsBlogs.in`
- **travels**:
  - *content*: a database with multiple blogs
    - two blogs
    - multiple posts and comments
    - nested comments
    - deleting posts and comments
  - *run*: `python frontEnd.py < testFiles/travelBlogs.in 2>&1 testFiles/grader.travelBlogs.out`
  - *verify*: `diff testFiles/grader.travelBlogs.out testFiles/travelBlogs.in`
- **bad**:
  - *content*: handles errors and bad requets
    - bad commands
    - bad permalink
    - acting on a deleted comment/blog
    - post with an existing permalink
  - *run*: `python frontEnd.py < testFiles/badBlogs.in 2>&1 testFiles/grader.badBlogs.out`
  - *verify*: `diff testFiles/grader.badBlogs.out testFiles/badBlogs.in`


## Notes
- Schema Design: We considered embeding our posts and comments but decided agains it so we could more easily seach the documents directly with the permalink. We decided on created three collection, `blogs`, `posts`, and`comments`. Each blog document contains a list of post permalinks contained inside it, each post document contains a list of comment permalinks contained inside it, and each comment document contains a list of replied comments permalinks contained inside it,
- In delete, we assume that only the body of the post/comment is deleted and the post title as well as all comments/replies remain intact; We also assume that anyone may delete a post or comment, even if they are not the author. For posts - timestamp is updated. For comments - we cannot change the permalink (it's permanent!) so we add a new timestamp field
- We standardized post permalinks to reference the post's title. This aligns with the lab specs, does not allow for duplicate posts within a blog to have the same title, and furthermore conflicts with the example test provided in the specs. Ensure during testing, when attempting to comment on or delete a post, that the permalink properly refers to the post's title, rather than its timestamp.