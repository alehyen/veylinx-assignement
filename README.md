## Endpoints
- POST api/create_user/: allow to create a user with username and password provided in the body
- POST api/token/:  authenticate a user, username and password should be provided in the body
- POST api/token/refresh/: get a new access token based on a refresh token provided in the body
- POST api/posts/: create a new post. Should have text in the body
- PUT api/posts/: update the text of a post. id_post and text should be provided in the body
- DELETE api/posts/: mark a post as deleted (soft delete). id_post should be provided in the body
- GET api/posts/: get the last posts with pagination, params page and page_size allow to choose the page and number of posts per page (20 by default)
- GET api/users/<user_id>/posts: get all posts of a user with pagination

## Thoughts about scaling

the soft delete can cause some performance issues when considering important data in the post model, because there is always a filtering by the `deleted` field,
one solution will be creating search indexes on the `deleted` field, or creating a separate table
to store the deleted posts and physically delete them from the post table to avoid the extra filtering

# Tests
to run the tests simply type `pytest` in the root of the project

#### Note: I'll be updating this readme gradually when adding new features