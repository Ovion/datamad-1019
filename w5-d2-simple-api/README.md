# Docker Commands
- Compile docker image with tag name `<tag_name>`: `docker build -t <tag_name> .`
- Run the created image: `docker run <tag_name>`
- Run in interactive mode (if you have an `input()`): `docker run -it <tag_name>`
- Run container in background (deatatched mode): `docker run -d <tag_name>`
- Remove an existing image: `docker rmi <tag_name>`
- Run with attatched ports: `docker run -p 8080:8080 <tag_name>`
- List all images: `docker images`
- List all running containers: `docker ps`

**NOTE:** Use `kitematic` app to have a more visual appealing interface to docker.


# Deploy en heroku
**WARNING** Debe de ser un repositorio nuevo de git solo con el codigo del proyecto

**Checklist:** 
1. Check that you have installed heroku cli in your terminal [https://devcenter.heroku.com/articles/heroku-cli]
2. Ensure user is logged in first with: `heroku login`

3. Then deploy the app with:
3.1. `heroku create <app_name>`
3.2. `heroku container:push api --app <app_name>`
3.3. `heroku container:release api --app <app_name>`

4. Open heroku control panel in the website and change environment variables in settings tab.