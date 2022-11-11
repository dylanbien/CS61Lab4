from pprint import pprint

def findBlog(blogs, posts, comments, params):

    # check params
    if len(params) != 3:
        print("error: incorrect number of params")
        return

    # parse params
    blogName = params[1]
    searchStr = params[2]

    # find and print blog
    result = list(blogs.find({"_id": blogName}))
    if not result:
        print("error: blog does not exist")
        return
    else:
        blog = result[0]
        print("\nin " + blog.get("_id") + ":\n")

    # find and print posts
    matchPosts = list(posts.find({"blog": blogName, "postBody": {"$regex": searchStr}, "deleted": {"$exists": False}}))
    matchComments = list(comments.find({"blog": blogName, "comment": {"$regex": searchStr}, "deleted": {"$exists": False}}))
    
    if not matchPosts and not matchComments:
        print("- - - -")
        print("no search results\n")
    else:
        if matchPosts:
            print("- - - -")
            print("posts matching search:\n")
            for post in matchPosts:
                
                title = post.get("title")
                userName = post.get("userName")
                tags = post.get("tags")
                permalink = post.get("_id")
                timestamp = post.get("timestamp")
                body = post.get("postBody")

                print("\t- - - -")
                print("\ttitle: " + title)
                print("\tuserName: " + userName)
                if tags is not None:
                    print("\ttags: " + tags)
                print("\tpermalink: " + permalink)
                print("\ttimestamp: " + timestamp)
                print("\tbody:\n\t  " + body + "\n")
        else:
            print("- - - -")
            print("no posts matching search\n")
        
        if matchComments:
            print("- - - -")
            print("comments matching search:\n")
            for comment in matchComments:
                userName = comment.get("userName")
                permalink = comment.get("_id")
                body = comment.get("comment")
                
                print("\t- - - -")
                print("\tuserName: " + userName)
                print("\tpermalink: " + permalink)
                print("\tcomment:\n\t  " + body + "\n")
        else:
            print("- - - -")
            print("no comments matching search\n")