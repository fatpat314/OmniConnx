#TODO#



## Separate listings and posts by user type and filter the results

## Next steps:

## Installed django-comments-xtd and added dependencies; when it's time to implement commenting, follow the instructions as of step 10 in https://django-comments-xtd.readthedocs.io/en/latest/quickstart.html#quick-start-guide

## once above is implemented, here's how to plug in the comments: https://pythoneatstail.com/en/overview-all-articles/allowing-users-comment-your-site-django-comments-xtd/

## styling tools stash: 
## 
## currently trying to have home page logo smooth-scroll to the login form at accounts/login/?next=/index/ | following this: https://css-tricks.com/almanac/properties/s/scroll-behavior/


## List of Medical Specialties and Subspecialties: https://www.sgu.edu/blog/medical/ultimate-list-of-medical-specialties/

## I've fixed the top navbar in place, but need to figure out how to get the posts to scroll up underneath it like the image does.

## I made the sidenav a tab that stays fixed on the left hand center of the screen; next im going to change the way the tabs look, change the categories, and have the subcategories appear to the right when hovering over the category

## we don't need to keep “listing_card.html”, which is where you go when clicking “read more” on a post.
### the ‘read more’ link, should only appear when there’s not enough space in the area of the posting to show its entire contents at once, so when clicked it will expand the area to reveal all its contents at once. on the same page. 

### as in: say the parameters of each post is 200x400; someone posts a long-ass paragraph that would need a space that’s 250x450 to fit, so in that case what we see initially is just part of the paragraph that fits our 200x400 box, with the ‘read more’ link in the bottom right corner of the box.

### when the read more link is clicked, the box should expand to 250x450 to show the entire paragraph at once (or however much space the content needs - we can make it responsive)

### then we need a ‘close’ link to revert the box and its content back to its original size.

## next, there's the 'Add Comment' box, which currently only appears on that seperate page when we click 'read more'. 

### what we want is both the 'add comment' link, as well as an indicator showing how many comments are currently on that post, to appear in the lower left-hand corner of the post; 

### when 'add comment' is clicked, then the user can either be directed to the seperate 'add comment' page as it currently appears, or we can have the add comment text box pop up right there and once a comment is added, the indicator will go up one (i.e."comments: 1"), and when the indicator is clicked, the comment_view field can also pop up right there over the post, where it can be read and have more comments added to the thread.
