# CS61Lab4

Note: In delete, we assume that only the body of the post/comment is deleted and the post title as well as all comments/replies remain intact; We also assume that anyone may delete a post or comment, even if they are not the author. For posts - timestamp is updated. For comments - we cannot change the permalink (it's permanent!) so we add a new timestamp field

Note: We standardized post permalinks to reference the post's title. This aligns with the lab specs, does not allow for duplicate posts within a blog to have the same title, and furthermore conflicts with the example test provided in the specs. Ensure during testing, when attempting to comment on or delete a post, that the permalink properly refers to the post's title, rather than its timestamp.