# CS61Lab4

## Build/Run 
To run the front-end application, ensure that you are in a python environment for databases (as described in Lab 0) and that the environment has been activated. From there, run `python3 frontEnd.py` to load the application, and enter inputs via the command line as prompted.

## Testing: 
The provided testfiles are:

- **politics**
  - *content*: an attempt to replicate the example provided in the lab specs, with the addition of the find query
  - *run*: `python frontEnd.py < testing/inputs/politicsBlogs.in > testing/outputs/grader.politicsBlogs.out 2>&1`
  - *verify*: `diff testing/outputs/grader.politicsBlogs.out testing/outputs/politicsBlogs.out`
- **travels**:
  - *content*: a database with multiple blogs
    - two blogs
    - multiple posts and comments
    - nested comments
    - deleting posts and comments
  - *run*: `python frontEnd.py < testing/inputs/travelBlogs.in > testing/outputs/grader.travelBlogs.out 2>&1`
  - *verify*: `diff testing/outputs/grader.travelBlogs.out testing/outputs/travelBlogs.out`
- **bad**:
  - *content*: handles errors and bad requests
    - bad commands
    - bad permalink
    - acting on a deleted comment/blog
    - post with an existing permalink
  - *run*: `python frontEnd.py < testing/inputs/badBlogs.in > testing/outputs/grader.badBlogs.out 2>&1`
  - *verify*: `diff testing/outputs/grader.badBlogs.out testing/outputs/badBlogs.out`


## Notes
- Schema Design: We considered embedding our posts and comments, but decided against it so we could more easily search the documents directly with the permalink. We created three collections, `blogs`, `posts`, and `comments`. Each blog document references a list of post permalinks, each post document references a list of comment permalinks, and each comment document references a list of replied comment permalinks.
- In delete, we assume that only the body of the post/comment is deleted and the post title as well as all comments/replies remain intact. The deleted timestamp is noted for both posts and comments inside the new post/comment body.
- We standardized post permalinks to reference the post's title. This aligns with the lab specs, though does not allow for duplicate posts within a blog to have the same title and furthermore conflicts with the example test provided in the specs. Ensure during testing, when attempting to comment on or delete a post, that the permalink properly refers to the post's title, rather than its timestamp.
- Extra Credit: The extra credit was completed in `find.py` and is tested in the politics blog for the key word `hullabaloo`