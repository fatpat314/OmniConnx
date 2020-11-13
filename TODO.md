#TODO#



## Separate listings and posts by user type and filter the results

## Next steps:

## Installed django-comments-xtd and added dependencies; when it's time to implement commenting, follow the instructions as of step 10 in https://django-comments-xtd.readthedocs.io/en/latest/quickstart.html#quick-start-guide

## once above is implemented, here's how to plug in the comments: https://pythoneatstail.com/en/overview-all-articles/allowing-users-comment-your-site-django-comments-xtd/


<!-- GSC -->
##  we don't need to keep the page,where you're sent when clicking “read more” on a post.

 <!-- GSC  -->
### the ‘read more’ link, should only appear when there’s not enough space in the area of the posting to show its entire contents at once, so when clicked it will expand the area to reveal all its contents at once. on the same page. 

<!-- GSC -->
###  as in: say the parameters of each post is 200x400; someone posts a long-ass paragraph that would need a space that’s 250x450 to fit, so in that case what we see initially is just part of the paragraph that fits our 200x400 box, with the ‘read more’ link in the bottom right corner of the box.

<!-- GSC -->
###  when the read more link is clicked, the box should expand to 250x450 to show the entire paragraph at once (or however much space the content needs - we can make it responsive) 

###  https://www.w3schools.com/howto/howto_js_read_more.asp

### then we need a ‘close’ link to revert the box and its content back to its original size.

## next, there's the 'Add Comment' box, which currently only appears on that seperate page when we click 'read more'. 

### what we want is both the 'add comment' link, as well as an indicator showing how many comments are currently on that post, to appear in the lower left-hand corner of the post; 

### when 'add comment' is clicked, we can have the add comment text box pop up right there and once a comment is added, the indicator will go up one (i.e."comments: 1"), and when the indicator is clicked, the comment_view field can also pop up right there over the post, where it can be read and have more comments added to the thread.

## Home Page

### GSC rather than scrolling, i'm scoing to make an 'enter' button that when clicked either has a small login form pop up on the same page, or maybe directs the user immediately to 'About Us', and integrate the login/signup on that page. we'll see. 


### GSC Button on my-invites page when its empty, that leads to profile_list
