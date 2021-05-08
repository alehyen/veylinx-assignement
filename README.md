## Endpoints
- POST api/create_user/: allow to create a user with username and password provided in the body
- POST api/token/:  authenticate a user, username and password should be provided in the body
- POST api/token/refresh/: get a new access token based on a refresh token provided in the body
- POST api/posts/: create a new post with the associated hashtags. Should have text in the body
- PUT api/posts/: update the text of a post. id_post and text should be provided in the body
- DELETE api/posts/: mark a post as deleted (soft delete). id_post should be provided in the body
- GET api/posts/: get the last posts with pagination, params page and page_size allow to choose the page and number of posts per page (20 by default)
- GET api/users/<user_id>/posts: get all posts of a user with pagination
- GET api/hashtags/<hashtag>/posts/: get all posts with for a particular hashtag with pagination
- GET api/popular_hashtags/: get the 5 most popular hashtags

## Hashtag system
I didn't implement the question 5 and 6 of the hashtag system, just because it will require 
creating a custom user model with a OneToOneField to the built-in User model, and a ManytoMany
relathionship to the hashtag table to store favorite hashtags, and then to add/delete favorites hashtags 
is a simple crud and to get posts from favorite hashtags we can re-use the `api/hashtags/<hashtag>/posts/` endpoint

## Celery
for the questions that requires sending an email I created just the signature of the functions,
because sending an email will require configuring and email server which I believe is not relevant 
for the purpose of the assignment.

for the periodic task I just configured it in the CELERY_BEAT_SCHEDULE setting, however we can create 
the schedule in the database and configure celery beat to fetch the periodic tasks from the database
## Thoughts about scaling

- the soft delete can cause some performance issues when considering important data in the post model, because there is always a filtering by the `deleted` field,
one solution will be creating search indexes on the `deleted` field, or creating a separate table
to store the deleted posts and physically delete them from the post table to avoid the extra filtering
  
- I've choosen to make a ManytoMany relationship between posts and hashtags to avoid storing 
duplicated hashtags and just reference them in the post, this might cause performance problems
  when considering a very important number of hashtags because there is a filtering with posts that contain a specific 
  hashtag, and that require a double join of the hashtag and post table, same for the most popular hashtags query,
  a need for and index search of the field `name` of the hashtag table might be a good solution

# Tests
to run the tests simply type `pytest` in the root of the project

#### Note: I'll be updating this readme gradually when adding new features